from django.contrib.auth.hashers import check_password
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError

from .constants import CACHE_TTL
from .tasks import send_email_otp
from users.authenticators import Token
from users.models import User
from .utils import create_random_otp


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        email = validated_data.get('email')
        if User.objects.filter(email=email):
            raise ValidationError
        return super().create(validated_data)


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email')


class ConfirmCodeSerializer(serializers.Serializer):
    code = serializers.CharField(read_only=True)
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email, password = attrs.get('email'), attrs.get('password')
        user = get_object_or_404(User, email=email)
        if not check_password(password, user.password):
            raise ValidationError('Wrong password.')
        return super().validate(attrs)

    def create(self, validated_data):
        email = validated_data.get('email')
        code = create_random_otp()
        cache.set(email, code, CACHE_TTL)
        send_email_otp(email, code)
        validated_data['code'] = code
        return validated_data


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True, source='key')
    email = serializers.CharField(write_only=True)
    otp = serializers.CharField(write_only=True)

    def validate(self, attrs: dict):
        email, otp = attrs.get('email'), attrs.get('otp')
        cache_otp = cache.get(email)
        if not cache_otp:
            raise NotFound('Confirmation code has probably expired.')
        if otp != cache_otp:
            raise ValidationError('Wrong code.')
        cache.delete(email)
        user = get_object_or_404(User, email=email)
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data.pop('user')
        token, status = Token.objects.get_or_create(user=user)
        return token

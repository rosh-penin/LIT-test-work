from rest_framework import mixins
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.viewsets import GenericViewSet

from .serializers import ConfirmCodeSerializer, TokenSerializer, UserSerializer
from users.models import User


class UserViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  GenericViewSet):
    """
    Similar to ModelViewSet but without list() action.
    Added more actions. All actions listed in the router.
    """
    queryset = User.objects.all()

    def get_object(self):
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied()
        if not User.objects.filter(email=user.email).exists():
            raise NotFound()
        return user

    def get_serializer_class(self):
        if self.action == 'login':
            return ConfirmCodeSerializer
        if self.action == 'confirm':
            return TokenSerializer
        return UserSerializer

    def login(self, request):
        """
        Call self.create() method with different serializer provided.
        Right now it returns serializer.data with email and code.
        And also sends code to user via email.
        """
        return self.create(request)

    def confirm(self, request):
        """
        Call self.create() method with different serializer provided.
        Takes email and OTP fields as request body and returns Token.
        """
        return self.create(request)

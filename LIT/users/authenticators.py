from django.db.models import CASCADE, OneToOneField
from rest_framework.authentication import TokenAuthentication as TknAuthExample
from rest_framework.authtoken.models import Token as TokenExample

from .models import User


class Token(TokenExample):
    """
    Overrided rest_framework.authtokens Token model with custom one.
    This model points to custom User model.
    """
    user = OneToOneField(
        User,
        CASCADE,
        related_name='auth_token',
        verbose_name='User'
    )


class TokenAuthentication(TknAuthExample):
    """
    Overrided rest_framework.authentication TokenAuthentication class.
    This class points to custom Token model declared above.
    """
    model = Token

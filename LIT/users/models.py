from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    """
    Model for basic user implementation.
    Created from scratch, not inherited from AbstractUser.
    Used standard django password hashing.
    """
    email = models.EmailField('Email address', unique=True)
    password = models.CharField('Password', max_length=200)
    is_anonymous = False
    is_authenticated = True
    is_active = True

    class Meta:
        ordering = ('email',)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)

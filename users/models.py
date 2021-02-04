from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
                                       BaseUserManager, \
                                       PermissionsMixin


class MyUserManager(BaseUserManager):
    """Class for manage users"""

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("You don't enter Email")
        if not username:
            raise ValueError("You don't enter Login")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


def create_user(self, email, username, password):
    """To create simple user"""

    return self._create_user(email, username, password,
                             is_staff=True,
                             is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)  # activate status
    is_staff = models.BooleanField(default=False)  # admin status

    USERNAME_FIELD = 'email'  # for address to user
    REQUIRED_FIELDS = ['username']  # list names field for Superuser

    def __str__(self):
        return self.username

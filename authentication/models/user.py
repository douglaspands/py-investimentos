# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from core.models.base import BaseModel


# class User(AbstractBaseUser, PermissionsMixin, BaseModel):
class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    person = models.OneToOneField("person.Person", on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

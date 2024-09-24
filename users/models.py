from enum import unique

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms.fields import CharField
from django_countries.fields import CountryField

NULLABLE = {'null':True, 'blank':True}

class User (AbstractUser):
    username = None
    email = models.EmailField(unique=True,  verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    phone = models.CharField(max_length=30, **NULLABLE, verbose_name='телефон')
    country = CountryField()
    token = models.CharField(max_length=100, **NULLABLE, verbose_name='токен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


import random
import string
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

    @staticmethod
    def generate_password(length: int):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        return password

    @property
    def is_moderator(self):
        if (self.has_perm('catalog.can_edit_description') and
                self.has_perm('catalog.can_edit_category') and
                self.has_perm('catalog.can_published')):
            return True
        return False


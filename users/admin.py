from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    filter_vertical = ['groups']

    class Meta:
        verbose_name='пользователь'
        verbose_name_plural='пользователи'



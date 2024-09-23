from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from users.forms import ProfileUpdateForm
from views import menu


class LoginView(BaseLoginView):
    template_name = 'users/user_form.html'
    extra_context = {
        'menu': menu,
        'title_form': 'Вход на сайт'
    }

class ProfileUpdateView(UpdateView):
    model =  get_user_model()
    form_class = ProfileUpdateForm
    template_name = 'users/user_form.html'
    extra_context = {
        'menu': menu,
        'title_form': 'Профиль пользователя'
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user


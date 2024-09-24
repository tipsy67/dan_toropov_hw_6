from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class ProfileUpdateForm(forms.ModelForm):

    email = forms.EmailField(disabled=True)

    class Meta:
        model = get_user_model()
        fields =('email', 'first_name', 'last_name', 'phone', 'country', 'avatar')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields =('email', 'first_name', 'last_name', 'password1', 'password2', 'country')
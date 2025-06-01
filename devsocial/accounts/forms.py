from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)

"""Module for user form."""

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput


class CreateUserForm(UserCreationForm):
    """Form for creating a new user with additional fields."""

    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    """
    Form for user login.
    """

    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password")

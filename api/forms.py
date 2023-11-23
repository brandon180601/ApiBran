from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Incluye 'password2'

class InicioSesionForm(forms.Form):
    usuario = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
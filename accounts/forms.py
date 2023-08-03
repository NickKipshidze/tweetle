from django.contrib import auth
from django.contrib.auth import forms

class SignUpForm(forms.UserCreationForm):
    class Meta:
        model = auth.get_user_model()
        fields = ("username", "email", "password1", "password2")

class LogInForm(forms.AuthenticationForm):
    class Meta:
        model = auth.get_user_model()
        fields = ("username", "password")
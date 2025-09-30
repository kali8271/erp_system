# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # your custom User model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "is_staff", "is_active"]

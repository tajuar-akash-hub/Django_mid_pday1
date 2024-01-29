from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

from django import forms
from Library_Management_App.models import Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Book_Form(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
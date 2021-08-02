from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser , University
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2','email', 'studenttype','university',
         'studentnumber','mentor_check','name', 'major','highschool','entrancetype','image',]


class UnivesityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['univer',]


class Change_emailForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']

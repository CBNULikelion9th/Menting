from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser 
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2','email', 'studenttype','university',
         'studentnumber','mentor_check','name', 'major','highschool','entrancetype','image',]



class Change_emailForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']

from django import forms
from django.db.models import fields
from .models import Post, Comment, Post2, Mentor

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content']

class PostForm2(forms.ModelForm):   

    class Meta:
        model = Comment
        fields = ['content']

class PostForm3(forms.ModelForm):

    class Meta:
        model = Post2
        fields = ['title','content']

class MentorForm(forms.ModelForm):

    class Meta:
        model = Mentor
        fields = ['username','email']
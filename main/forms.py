from django import forms
from django.db.models import fields
from .models import Post, Comment, Post2, Mentor, Recomment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content']
        widgets = {
            'title': forms.Textarea(attrs={'rows':1, 'cols':165}),
            'content': forms.Textarea(attrs={'rows':4, 'cols':165}),
        }

class PostForm2(forms.ModelForm):   

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':5, 'cols':165}),
        }

class RecommentForm(forms.ModelForm):   

    class Meta:
        model = Recomment
        fields = ['content','comment']

class PostForm3(forms.ModelForm):

    class Meta:
        model = Post2
        fields = ['title','content']
        widgets = {
            'title': forms.Textarea(attrs={'rows':1, 'cols':165}),
            'content': forms.Textarea(attrs={'rows':4, 'cols':165}),
        }

class MentorForm(forms.ModelForm):

    class Meta:
        model = Mentor
        fields = ['username','email']
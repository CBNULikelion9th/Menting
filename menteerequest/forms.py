from django import forms
from .models import Mentee_request, Comment

class Mentee_requestForm(forms.ModelForm):

    class Meta():
        model = Mentee_request
        fields = ['mentee_highschool','grade','mentee_major','mentee_entrancetype','counsel']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
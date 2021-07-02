from django import forms
from .models import Mentee_request, Response, Point



class Mentee_requestForm(forms.ModelForm):

    class Meta():
        model = Mentee_request
        fields = ['mentee_highschool','grade','mentee_major','mentee_entrancetype','counsel']

class ResponseForm(forms.ModelForm):

    class Meta:
        model = Response
        fields = ('text',)

class PointForm(forms.ModelForm):

    class Meta:
        model = Point
        fields = ('grade',)
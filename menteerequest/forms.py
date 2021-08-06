from django import forms
from .models import Mentee_request, Response, Point



class Mentee_requestForm(forms.ModelForm): #멘틸 요청서 입력사항

    class Meta():
        model = Mentee_request
        fields = ['mentee_highschool','grade','mentee_major','mentee_entrancetype','counsel']

class ResponseForm(forms.ModelForm):    # 수락거절 폼

    class Meta:
        model = Response
        fields = ('text',)

class PointForm(forms.ModelForm):   # 메팅 완료후 평점을 남길 폼

    class Meta:
        model = Point
        fields = ('grade',)
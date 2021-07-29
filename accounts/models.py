from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    university = models.CharField(max_length=50,default="멘토만 작성")
    name = models.CharField(max_length=50)
    studentnumber = models.IntegerField(default = 0)
    major = models.CharField(max_length=50,default="멘토만 작성")
    entrancetype = models.CharField(max_length=50,default="멘토만 작성")
    mentor_check = models.BooleanField(default=False) # 운영진이 확인한 멘토만 true
    studenttype = models.BooleanField(default=False)   #가입시 멘토로 가입하면 체크
    image = models.ImageField(blank = True, upload_to = 'certificate') #멘토 가입시 대학 재학 서류 
    HIGHSCHOOL_CHOICES = (
		('일반고', '일반고'),('특목고', '특목고'),('특성화고', '특성화고'),('자공고, 자사고', '자공고, 자사고'),('기타', '기타')
    )
    highschool = models.CharField(max_length=10, choices=HIGHSCHOOL_CHOICES, blank=True)
    grade = models.IntegerField(default = 0)    # 유저가 평점을 매디면 여기로 들어온다 기존 + 매긴 평점
    count = models.IntegerField(default = 0)    # 유저들이 평점을 매긴 횟수
    avg = models.IntegerField(default = 0)      # count와 grade를 합쳐서 평균을 나타냄 밖에 보여주는 평점

class University(models.Model):  #첫 홈페이지에서 대학 검색을 위해 일시적으로 만든 모델 지도검색과 연결시 필요 없어짐

    univer = models.CharField(max_length=50)

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    university = models.CharField(max_length=50,default="멘토만 작성")
    name = models.CharField(max_length=50)
    studentnumber = models.IntegerField(default = 0)
    major = models.CharField(max_length=50,default="멘토만 작성")
    entrancetype = models.CharField(max_length=50,default="멘토만 작성")
    mentor_check = models.BooleanField(default=False)
    studenttype = models.BooleanField(default=False)
    image = models.ImageField(blank = True, upload_to = 'certificate')
    HIGHSCHOOL_CHOICES = (
		('일반고', '일반고'),('특목고', '특목고'),('특성화고', '특성화고'),('자공고, 자사고', '자공고, 자사고'),('기타', '기타')
    )
    highschool = models.CharField(max_length=10, choices=HIGHSCHOOL_CHOICES, blank=True)
    grade = models.IntegerField(default = 0)
    count = models.IntegerField(default = 0)
    avg = models.IntegerField(default = 0)

class University(models.Model):

    univer = models.CharField(max_length=50)

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50,default="멘토만 작성")
    name = models.CharField(max_length=50)
    studentnumber = models.IntegerField(default = 0)
    major = models.CharField(max_length=50,default="멘토만 작성")
    entrancetype = models.CharField(max_length=50,default="멘토만 작성")
    highschool = models.CharField(max_length=50,default="멘토만 작성")
    studenttype = models.BooleanField(default=False)
    image = models.ImageField(blank = True, upload_to = 'certificate')

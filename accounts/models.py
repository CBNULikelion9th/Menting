from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    studentnumber = models.IntegerField(default = 0)
    major = models.CharField(max_length=50)
    entrancetype = models.CharField(max_length=50)
    highschool = models.CharField(max_length=50)


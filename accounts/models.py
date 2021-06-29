from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    nickname = models.CharField(max_length=100, unique = True)
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
    gradepoint = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    


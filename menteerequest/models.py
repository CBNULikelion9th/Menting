from django.db import models


# Create your models here.
class Mentee_request(models.Model):
    
    mentee_major = models.CharField(max_length=50)
    mentee_entrancetype = models.CharField(max_length=50)
    counsel = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    mentee = models.CharField(max_length=15)
    mentor = models.CharField(max_length=15)
    HIGHSCHOOL_CHOICES = (
		('일반고', '일반고'),('특목고', '특목고'),('특성화고', '특성화고'),('자공고, 자사고', '자공고, 자사고'),('기타', '기타')
    )
    mentee_highschool = models.CharField(max_length=10, choices=HIGHSCHOOL_CHOICES)
    GRADE_CHOICES = (
		('1', 1),('2', 2),('3', 3),('기타', '기타')
    )
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
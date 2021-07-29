from django.db import models
from django.conf import settings

# Create your models here.
class Mentee_request(models.Model):   #요청서
    
    mentee_major = models.CharField(max_length=15)
    mentee_entrancetype = models.CharField(max_length=50)
    counsel = models.TextField()  #상담 내용
    created_at = models.DateTimeField(auto_now_add = True)

    mentee = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank =True)  #작성자 글쓴 유저와 1:m으로 연결

    mentor = models.CharField(max_length=15)
    HIGHSCHOOL_CHOICES = (
		('일반고', '일반고'),('특목고', '특목고'),('특성화고', '특성화고'),('자공고, 자사고', '자공고, 자사고'),('기타', '기타')
    )
    mentee_highschool = models.CharField(max_length=10, choices=HIGHSCHOOL_CHOICES)
    GRADE_CHOICES = (
		('1', 1),('2', 2),('3', 3),('기타', '기타')     
    )
    grade = models.CharField(max_length=4, choices=GRADE_CHOICES)
    mentor_email = models.CharField(max_length=50)  #이메일 전송을 위해 멘토의 이메일을 저장
    finish_check = models.BooleanField(default=0)
    

class Response(models.Model):
    post = models.ForeignKey('Mentee_request', on_delete=models.CASCADE, related_name='responses')
    author = models.CharField(max_length=100)
    text = models.TextField(null = True, blank = True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text

class Point(models.Model): 
    GRADE_CHOICES = (
		('1', 1),('2', 2),('3', 3),('4', 4),('5', 5)  #멘토에게 줄 평점
    )
    grade = models.CharField(max_length=5, choices=GRADE_CHOICES)
    username = models.CharField(max_length=20)
    point = models.IntegerField(default=0)
  
class Mname(models.Model):  
  username = models.CharField(max_length=20,blank = True)
from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null =True)
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, null = True, blank = True, on_delete=models.CASCADE)
    name = models.TextField()
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recomment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    name2 = models.TextField(null =True)
    content = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

class Post2(models.Model):
    username= "STAFF"
    title = models.CharField(max_length=20, default = '')
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True, null = True)
    updated_at = models.DateTimeField(auto_now=True, null = True)

class Mentor(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


    

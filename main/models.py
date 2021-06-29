from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, null = True, blank = True, on_delete=models.CASCADE)
    name = models.TextField()
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post2(models.Model):
    username= "STAFF"
    title = models.CharField(max_length=20, default = '')
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True, null = True)
    updated_at = models.DateTimeField(auto_now=True, null = True)
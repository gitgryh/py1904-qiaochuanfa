from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ads(models.Model):
    img=models.ImageField(upload_to="ads")
    desc=models.CharField(max_length=10)
    index=models.IntegerField(default=0)

class Category(models.Model):
    title=models.CharField(max_length=40)

class Tag(models.Model):
    title=models.CharField(max_length=40)
class Article(models.Model):
    title=models.CharField(max_length=40)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    creat_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    views=models.IntegerField(default=0)
    body=models.TextField()
    tag=models.ManyToManyField(Tag)



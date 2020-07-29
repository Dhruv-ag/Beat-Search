from django.db import models
class Post(models.Model):
    sname=models.TextField(max_length=100)
    aname=models.CharField(max_length=100)
    limit=models.IntegerField()
    

# Create your models here.

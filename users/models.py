# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpeg',upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
# Create your models here.

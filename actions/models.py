from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio =  models.TextField(max_length=50,default='')
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    country = models.TextField(max_length=50, default='')
    def __str__(self):
        return f'{self.user.username} Profile'



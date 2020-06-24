from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    user_img = models.ImageField(upload_to='user/images')
    interest = models.TextField(max_length=100,default='')
    birth_date = models.DateField(null=True, blank=True)

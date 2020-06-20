from django.db import models

# Create your models here.
class Pic(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=100,default='')
    img_name = models.CharField(max_length=50,default='')
    img_desc = models.CharField(max_length=500,default='')
    img = models.ImageField(upload_to='post/images',default='')
    tags = models.CharField(max_length=100,default='')
    web_link = models.CharField(max_length=500,default='')
    pub_date = models.DateTimeField(auto_now=True)




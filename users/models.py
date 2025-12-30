from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=15,blank=True,null=True,unique=True)
    profile_picture=models.ImageField(upload_to='profile_images/',blank=True,null=True,default='profile_images/default_img.png')

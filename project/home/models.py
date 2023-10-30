from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
# Create your models here.


class UserModel(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True,unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class UserProfileModel(models.Model):
    profile = models.ImageField(upload_to='project/profile')
    phone = models.IntegerField()
    
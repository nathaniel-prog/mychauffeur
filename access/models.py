from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User ,null=True , on_delete=models.CASCADE)
    avatar = models.ImageField(default='nathan1.jpeg', upload_to='images/', null=True)

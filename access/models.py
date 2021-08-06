from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User ,null=True , on_delete=models.CASCADE)
    avatar = models.ImageField(default='user_anonimous.jpg', upload_to='images/', null=True)
    age = models.PositiveIntegerField(null=True , blank=True)
    email=models.EmailField(null=True , blank=True,unique=True)


    def __str__(self):
        return f'{self.user} profile'


def created_profile(sender, instance , created , **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('profile created')

post_save.connect(created_profile ,sender=User)


def update_profile(sender,instance , created, **kwargs):
    if created== False:
        instance.userprofile.save()
        print('profile update')

post_save.connect(update_profile , sender=User)

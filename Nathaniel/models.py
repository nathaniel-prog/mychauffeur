from django.db import models
from django.contrib.auth.models import User
from datetime import date
from twilio.rest import Client







class Post(models.Model):
    titre= models.CharField(max_length=150,default='it was nice', null=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    body= models.TextField(default='whats in your mind ')









class Chauffeur(models.Model):
    name= models.CharField(max_length=125 , null=False)
    date_of_birth=models.DateField(default=date.today())
    date_inscription=models.DateField(default=date.today())

    car= models.CharField(max_length=255 ,default='Regular car', null=False)



    def __str__(self):
        return str(self.name)

    def save(self , *args , **kwargs):
        if self.name:
            account_sid = 'AC0bfa41e3d8d3f121949b600d9b3d5831'
            auth_token = 'd06b042acf3776f1c57bf14278b8dbde'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'TKT FRERO ON VA CARTONNER C UNE QUESTION DE TEMPS {self.name}',
                from_='+12543312099',
                to=['+972585230351']
            )
            print(message.sid)

        return super().save(*args, **kwargs)


class Scores(models.Model):
    result= models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = 'AC0bfa41e3d8d3f121949b600d9b3d5831'
            auth_token = 'd06b042acf3776f1c57bf14278b8dbde'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body='Hi there! tomorow dont do couscous cause we are only 3 I think',
                from_='+972585230351',
                to='+972586040291'
        )
            print(message.sid)

        return super().save(*args,**kwargs)







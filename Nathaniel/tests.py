from django.test import TestCase
import datetime
import time
import requests

from .models import *





def ask_destinat(ville):
    r=Post.objects.filter(titre=ville)
    if r.count()>1:
        print('yes ')


ask_destinat('ashdod')



def delete(post):
    new_post= Post.objects.create(author=post)
    if new_post:
        new_post.delete()



if __name__ == '__main__':
    ask_destinat()
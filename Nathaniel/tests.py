from django.test import TestCase

from .models import *





def ask_destinat(ville):
    r=Post.objects.filter(titre=ville)
    if r.count()>1:
        print('yes ')


ask_destinat('ashdod')


if __name__ == '__main__':
    ask_destinat()
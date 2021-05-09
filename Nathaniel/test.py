import time
import datetime
import json

from findchauffeur.settings import *
from Nathaniel.models import Post






def bodek(ville):
    people= Post.objects.filter(titre=ville)

    if ville in people:
        return f'someone else look at {ville}'





def ask_destinat(ville):
    r=Post.objects.filter(titre=ville)
    for obj in r:
        if r.count()>1:
            return(obj.titre)


ask_destinat('ashdod')





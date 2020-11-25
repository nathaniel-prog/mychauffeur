from django import forms

from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Scores , Chauffeur , Post
from django.apps import apps







class SmsChauffeur(forms.ModelForm):
    class Meta:
        model= Chauffeur
        fields=['name' , 'date_of_birth', 'car' ]
















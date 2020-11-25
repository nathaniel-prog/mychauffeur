from django.urls import path

from . views import ChauffeurListView , InvidChauffeurView
from . import views
from django.conf import settings




urlpatterns = [

   path('home',views.test,name='home'),
   path('drivers', ChauffeurListView.as_view()),
   path('drivers<int:pk>',InvidChauffeurView.as_view(),name='driver'),
   path('sms',views.envoi_sms , name='sendsms'),
   path('radio', views.radio_label , name='radio')
]



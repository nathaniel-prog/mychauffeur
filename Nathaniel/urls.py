from django.urls import path

from . views import ChauffeurListView , InvidChauffeurView , HomeView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login as auth_login , authenticate
from django.contrib.auth.decorators import login_required




urlpatterns = [

   path('test',views.test,name='test'),
   path('drivers', ChauffeurListView.as_view(), name='drivers'),
   path('drivers<int:pk>',InvidChauffeurView.as_view(),name='driver'),
   path('sms',views.envoi_sms , name='sendsms'),
   path('radio', views.radio_label , name='radio'),
    path('hello', HomeView.as_view(),name='hello'),
    path('home2' ,views.home_2 , name='home2'),
    path('testing', views.testing , name='testing'),
    path('multiple', views.envoi_multiple, name='multiple')

    #path('pick<int:pk>', pickchauffeur(), name='pick')

]





if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)



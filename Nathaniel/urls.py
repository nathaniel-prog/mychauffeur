from django.urls import path

from . views import(ChauffeurListView ,
InvidChauffeurView ,
HomeView ,UpdatePostView,DetailPostView,
PostListView,CreatePostView, AllUserView,DetailUserView)
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login as auth_login , authenticate
from django.contrib.auth.decorators import login_required




urlpatterns = [

   path('test',views.test,name='test'),
   path('drivers', ChauffeurListView.as_view(), name='drivers'),
   path('drivers<int:pk>',InvidChauffeurView.as_view(),name='driver'),
    path('post/new',CreatePostView.as_view(), name='create'),
    path('post<int:pk>',DetailPostView.as_view(), name='postdetail'),
    path('post<int:pk>update',UpdatePostView.as_view(), name='postupdate'),
    path('postlist', PostListView.as_view(), name= 'list'),
    path('logout', views.logout_view , name='logout'),
   path('sms',views.envoi_sms , name='sendsms'),
    path('ask_desti', views.ask_dest , name='ask'),
    path('hello', HomeView.as_view(),name='hello'),
    path('home2' ,views.home_2 , name='home2'),
    path('multiple', views.envoi_multiple, name='multiple'),
    path('localisation', views.localisation_info, name='localisation'),
    path('try_local<int:pk>',views.try_local, name='trylocal'),

    path('where', views.where , name= 'where'),
    path('futur', views.effacer_donées, name='futur'),
    path('users', AllUserView.as_view(), name='users'),
    path('user<int:pk>',DetailUserView.as_view(), name='detail-user' ),
    path('account',views.account_setting , name= 'account')




    #path('pick<int:pk>', pickchauffeur(), name='pick')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)





if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)



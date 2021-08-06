from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register',views.register, name='register'),
    path('access',views.user_no_auth),
    path('login', LoginView.as_view(template_name='login.html') , name='login'),
    path('login_d', views.login_driver , name= 'login_d'),
    path('',views.welcome , name='welcome'),
    path('loginbis', views.loginbis , name='loginbis')





]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
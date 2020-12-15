from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from . import views

urlpatterns = [
    path('register',views.register, name='register'),
    path('d',views.user_no_auth),
    path('login', LoginView.as_view(template_name='login.html') , name='login'),
    path('login_d', views.login_driver)




]
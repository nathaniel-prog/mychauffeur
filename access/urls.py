from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from . import views

urlpatterns = [
    path('register',views.register, name='register'),]
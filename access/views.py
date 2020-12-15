from django.shortcuts import render
from .models import User
from django.contrib.auth import login as auth_login , authenticate
from .form import MyUserCreationForm
from .models import User
from django.http import HttpResponseRedirect


# Create your views here.


def register(request):
    if request.method == 'GET':
        form = MyUserCreationForm()
        return render(request, 'register.html', {'form': form})

    else:

        if request.method == 'POST':
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
            return HttpResponseRedirect('home2')


def user_no_auth(request):
    return render (request,'user_no_authenticate.html')


def log_in(request):
    return render(request, 'login.html'  )


def login_driver(request):
    return render(request, 'login_driver.html')


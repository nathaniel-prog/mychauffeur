from django.shortcuts import render
from .models import User
from django.contrib.auth import login as auth_login , authenticate
from .form import MyUserCreationForm , NewChauffeur , UserLoginForm
from Nathaniel.models import Driver
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
    if request.method == 'GET':
        form = NewChauffeur()
        return render(request, 'login_driver.html', {'form': form})

    else:

        if request.method == 'POST':
            form = NewChauffeur(request.POST)
            if form.is_valid():
                user = form.save()
            return HttpResponseRedirect('home2')


def loginbis(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'login_driver.html', {'form': form})

    else:

        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                user = form.clean()
            return HttpResponseRedirect('home2')


def welcome(request):
    if request.method=='GET':
        return render (request,'welcome.html')
    else:
        if request.method=='POST':
            query = request.POST["depart"]
            if query:
                depart= Driver.objects.filter(depart=query).count()
                arrive = Driver.objects.filter(arrivé=query)
                if depart >= 2:
                    choutaf= Driver.objects.filter(depart=query)
            context = {'choutaf':choutaf ,
                       'arrivé':arrive}
    return render(request,'welcome.html',context)


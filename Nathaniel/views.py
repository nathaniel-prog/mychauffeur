
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import login as auth_login

from django.contrib.auth import login as auth_login , authenticate
import asyncio
from django.contrib import messages
import datetime
from django.urls import reverse
from .models import Chauffeur , Score , Post , PhoneNumber , User
from django.views.generic import ListView, DetailView , TemplateView
from django.http import HttpResponse , HttpResponseRedirect
from .forms import SmsChauffeur , HomePost , Ask_destination
from .test import ask_destinat , bodek

# Create your views here.




def test(request):
    return HttpResponse('je ffffffouuuuu')


def listofuser(request):
    _all= User.objects.all()
    return render(request,'all_users.html', {'all': _all})








class ChauffeurListView(ListView):
    model = Chauffeur
    template_name = 'drivers.html'











def envoi_sms(request):
    if request.method == 'POST':
        form = SmsChauffeur(request.POST )
        if form.is_valid():
            form.save()
            return render(request, 'sms.html', {'form': form})
    else:
        form= SmsChauffeur()
        return render(request ,'sms.html',{'form':form} )



def ask_dest(request):
    if request.method == 'POST':
        form = Ask_destination(request.POST )
        titre= Post.objects.filter(titre=str(form))



        if form.is_valid():
            user=form.save()

            return render(request ,'ask_desti.html',{'form':form , 'titres':titre} )

    else:
        form= Ask_destination()
        return render(request ,'ask_desti.html',{'form':form} )






class InvidChauffeurView(DetailView):
    model = Chauffeur
    template_name = 'chauffeurs.html'



    def get_context_data(self, *args,**kwargs):
        context=super(InvidChauffeurView, self).get_context_data()
        stuff = get_object_or_404(Chauffeur, id=self.kwargs['pk'])
        choosen = stuff.save()
        context['choosen']= choosen


        return context



@login_required
def envoi_multiple(request):
    all = Chauffeur.objects.all()
    if request.method== 'GET':
        for obj in all:
            see=obj.save()
    
        return render(request,'multiple.html',{  'see':see })






def radio_label(request):
    context={}
    ch=Chauffeur.objects.all()
    context['chauffeurs']= ch

    return render(request,'radio.html',context)


def phone_number(request):
    context={}
    ph_ = PhoneNumber



class HomeView(TemplateView):
    template_name = 'start.html'



    def get(self,request):
        form = HomePost()
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form= HomePost(request.POST)
        if form.is_valid():
            text= form.cleaned_data('post')
        context={'form':form,'text':text}
        return render(request,self.template_name, context)


#def pickchauffeur(request,pk):
  # pick=get_object_or_404(Chauffeur,id=request.POST.get('gender'))
  # pick.name.add(request.user)
  # return HttpResponseRedirect(reverse('radio.html', args=[str(pk)]))



def home_2(request):
    return render(request , 'home2.html')


def auto_create(request):
    if request.method == 'GET':
        with open ('new_file.html', 'x') as f :
            f.read 



def localisation_info(request):
        _user =get_object_or_404(User,id=1)
        if _user:
            loc_post=Post.objects.get(author=_user)
            local=loc_post.localinfo()

        return render(request, 'localisation.html',{'local': local} ,{'loc_post':loc_post} )



def try_local(request,id):
    if request.method=='get':
        _user=User.objects.get(id=id)
        _post= Post.object.create(author=_user)
        if _post:
            _post.localinfo()
            return render(request, 'trylocal.html', {'user': _user , 'post': _post})


def where(request):
    if request.method == 'POST':
        query = request.POST["q"]
        archives = Post.objects.filter(titre=query).count()
        archive = Post.objects.filter(titre=query)
        if archives>=2:
            archive
        else:
            messages.error(request, 'no one go there today')
        return render(request,'where.html', {'archive': archive ,  'archives':archives })




    else :
        if request.method== 'GET':
            return render(request,'where.html', )

















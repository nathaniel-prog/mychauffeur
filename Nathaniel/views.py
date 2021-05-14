
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponseRedirect
from django.dispatch import Signal

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Chauffeur , Score , Post , PhoneNumber , User
from django.views.generic import ListView, DetailView , TemplateView
from django.http import HttpResponse
from .forms import SmsChauffeur , HomePost , ScoreForm

# Create your views here.




def test(request):
    return HttpResponse('je commence a comprendre git')

def testing(request):
    if request.method == 'POST':
        form_score=ScoreForm(request.Post)
        if form_score:
            if form_score.is_valid():
                inc_score=form_score+1
            return render(request , 'testscore.html',{'inc_score':inc_score})




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





class InvidChauffeurView(DetailView):
    model = Chauffeur
    template_name = 'chauffeurs.html'



    def get_context_data(self, *args,**kwargs):
        context=super(InvidChauffeurView, self).get_context_data()
        stuff = get_object_or_404(Chauffeur, id=self.kwargs['pk'])
        choosen = stuff.save()
        context['choosen']= choosen


        return context









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

def fixdate(request):
    if request.method == 'POST':
        query = request.POST["q"]

        if query:
            savedate = Chauffeur.objects.create(date=query, )
            return render(request ,'datehour.html' ,{'savedate': savedate})
    else:
        if request.method== 'GET':
            return render(request, 'datehour.html', )














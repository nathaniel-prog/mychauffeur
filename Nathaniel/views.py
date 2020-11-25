
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Chauffeur , Scores , Post
from django.views.generic import ListView, DetailView , CreateView
from django.http import HttpResponse
from .forms import SmsChauffeur

# Create your views here.




def test(request):
    return HttpResponse('je ffffff')


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


    def get_context_data(self,*args, **kwargs):
        context = super(InvidChauffeurView, self).get_context_data()
        stuff = get_object_or_404(Chauffeur, id=self.kwargs['pk'])
        call_chauffeur = stuff.delete()
        context['call_chauffeur'] = call_chauffeur

        return context




def delete_score(request, id):
    obj= get_object_or_404(Scores,id='id' )
    if request.method == 'POST':
        obj.delete()

    return render(request,'Nathaniel/selectoption.html', {'ws':ws})



def radio_label(request):
    context={}
    ch=Chauffeur.objects.all()
    context['chauffeurs']= ch
    return render(request,'radio.html',context)















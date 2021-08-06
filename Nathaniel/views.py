
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth import logout
from Nathaniel.insert_function import with_city
from access.models import UserProfile
from django.contrib.auth import login as auth_login
from django.contrib.auth import login as auth_login , authenticate
from django.contrib import messages
import datetime
from django.urls import reverse
from .models import Chauffeur , Score , Post , PhoneNumber , User
from django.views.generic import ListView, DetailView , TemplateView , CreateView
from django.http import HttpResponse , HttpResponseRedirect
from .forms import SmsChauffeur , HomePost , Ask_destination
from .test import ask_destinat , bodek
from django.contrib.auth import logout




def logout_view(request):
    logout(request)
    return redirect('welcome')





def test(request):
    if request.user.is_anonymous== False:
        return HttpResponse('je ffffffouuuuu')
    else:
        return redirect('login')


def listofuser(request):
    _all= User.objects.all()
    avatar=UserProfile.objects.all()
    return render(request,'all_users.html', {'all': _all , 'avatar':avatar})



def account_setting(request):
    return render(request, 'profile_setting.html')







@ login_required
def home_2(request):

    findlocal = with_city()
    return render(request, 'home2.html', {'findlocal': findlocal})


class PostListView(ListView):
    model=Post
    template_name = 'post_list.html'
    ordering = ['-titre']




class CreatePostView(CreateView):
    model = Post
    fields=['titre','body']
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class AllUserView(ListView):
    model=User
    template_name = 'user_list.html'


class DetailUserView(DetailView):
    model = User
    template_name = 'user_detail.html'





class ChauffeurListView(ListView):
    model = Chauffeur
    template_name = 'drivers.html'











def envoi_sms(request):
    if request.method == 'POST':
        form = SmsChauffeur(request.POST )
        if form.is_valid():
            form.cleaned_data
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
        form = Ask_destination()
        return render(request, 'ask_desti.html', {'form': form})










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


def effacer_donées(request):
    Nathaniel= User.objects.get(id=1)
    infoNath= Nathaniel.post_set.all()
    if request.method == 'GET':
        infoNath.delete()
        nath='nathaniel données effaées'
    return render(request, 'futur.html', {'nath':nath})



class CreatePost(CreateView):
    model=Post
    fields = ['titre','body','author']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)





























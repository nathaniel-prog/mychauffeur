from django import forms
from django.contrib.auth.forms import UserCreationForm , authenticate
from django.contrib.auth.models import User
from Nathaniel.models import Chauffeur
from access.models import UserProfile
from django.core.files.images import get_image_dimensions









class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']




class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    def clean(self , *args , **kwargs):
        username= self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password :
            user = authenticate(username=username , password=password)
            if not user:
                raise forms.ValidationError("this user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError('the passport does not match')
            if not user.is_active:
                raise forms.ValidationError('user is not active')


            return super(UserLoginForm,self).clean(*args , **kwargs)


class NewChauffeur(forms.ModelForm):
    class Meta:
        model = Chauffeur
        fields = ['name', 'num_phone' , 'car']




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ 'avatar', 'user']

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']






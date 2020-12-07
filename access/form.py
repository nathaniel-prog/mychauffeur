from django import forms
from django.contrib.auth.forms import UserCreationForm , authenticate
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']


class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


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

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms
from .validators import *

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
        

class RegisterForm(forms.Form):
    email = forms.EmailField(max_length = 50)
    password = forms.CharField(max_length = 50, widget=forms.PasswordInput)
    nume = forms.CharField(max_length = 50)
    
class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 50)
    password = forms.CharField(max_length = 50, widget=forms.PasswordInput)

class AddrForm(forms.Form):
    street = forms.CharField(max_length = 100)
    phone_number = forms.CharField(max_length = 10, validators=[phone])
    street_number = forms.IntegerField(validators=[poz])
    bloc = forms.IntegerField(validators=[poz])
    scara = forms.CharField(validators=[scara], max_length = 1)
    ap = forms.IntegerField(validators=[poz])
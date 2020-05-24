
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms


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
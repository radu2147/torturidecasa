from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Address
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
    email = forms.EmailField(max_length=50)
    nume = forms.CharField(max_length=50)

    def signup(self, request, user):
        adr = Address.objects.create(street="", phone_number="", scara="")
        user.nume = self.cleaned_data['nume']
        user.addr = adr
        user.save()

class AddrForm(forms.Form):
    street = forms.CharField(max_length = 100, required = False)
    phone_number = forms.CharField(max_length = 10, validators=[phone], required = False)
    street_number = forms.IntegerField(validators=[poz], required = False)
    bloc = forms.IntegerField(validators=[poz], required = False)
    scara = forms.CharField(validators=[scara], max_length = 1, required = False)
    ap = forms.IntegerField(validators=[poz], required = False)

class ChangeForm(forms.Form):
    nume = forms.CharField(max_length = 100, required = False)
    old_passwd = forms.CharField(max_length = 100, required = True)
    passwd = forms.CharField(max_length = 100, required = False, validators = [valid_pass])
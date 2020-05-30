from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model, logout

from .forms import *
from .validators import validate_passwds, valid_pass, valid_name
from .models import *
from HomePage.models import Produs
from Cart.models import *
from Cart.forms import *
from Personalize.models import *

# Create your views here.
class UserView(View):
    def get(self, request):
        form = AddrForm()
        addr = request.user.addr
        if request.user.is_authenticated:
            return render(request, 'extend_user.html', {'user': request.user, 'form' : form, 'addr' : addr})
        else:
            return redirect('/user/login')
    def post(self, request):
        if 'street' in request.POST.keys():
            form = AddrForm(request.POST)
            
            if form.is_valid():
                obj, crt = Address.objects.get_or_create(street = form.cleaned_data['street'], phone_number = form.cleaned_data['phone_number'], street_number = form.cleaned_data['street_number'], bloc = form.cleaned_data['bloc'], scara = form.cleaned_data['scara'], ap = form.cleaned_data['ap'])
                request.user.addr = obj
                request.user.save()
            addr = request.user.addr
            return render(request, 'extend_user.html', {'user': request.user, 'form' : form, 'addr' : addr})
        elif 'old_passwd' in request.POST.keys():
            form = ChangeForm(request.POST)
            
            if form.is_valid():
                if not validate_passwds(form.cleaned_data['old_passwd'], form.cleaned_data['passwd']):
                    return HttpResponse("Passwords do not match")
                if valid_pass(form.cleaned_data['passwd']):
                    request.user.password = form.cleaned_data['passwd']
                if valid_name(form.cleaned_data['nume']):
                    request.user.nume = form.cleaned_data['nume']
                request.user.save()
            addr = request.user.addr
            return render(request, 'extend_user.html', {'user': request.user, 'form' : form, 'addr' : addr})


class UserViewWish(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'wish_list.html', {'user': request.user, 'cos': WishList.objects.filter(email = request.user.email)})
        else:
            return redirect('/user/login')
        
class UserViewCart(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'cart.html', {'user': request.user, 'cos': Cart.objects.filter(email = request.user.email), 'price' : Cart.get_total(request.user.email)})
        else:
            return redirect('/user/login')
        
class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/user/myaccount")
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})
        
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            us = User.objects.create_user(email = form.cleaned_data['email'], password = form.cleaned_data['password'], nume=form.cleaned_data['nume'])
            us.save()
            us.active = True
            return redirect('/')
        else:
            form = RegisterForm()
            return render(request, 'registration/register.html', {'form': form})
        
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/user/myaccount")
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
        
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)    
                return redirect('/')
            else:
                return HttpResponse("STG")
        else:
            form = LoginForm()
            return render(request, 'registration/login.html', {'form': form})
class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')
    
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model, logout

from .forms import *
from .models import *
from Cart.models import *
from Personalize.models import *
from .utils import *

# Create your views here.
class UserView(View):
    '''
    Returns the user's page if the user is logged in else redirects to the login page
    '''
    def get(self, request):
        form = AddrForm()
        if request.user.is_authenticated:     
            return render(request, 'extend_user.html', {'user': request.user, 'form' : form, 'addr' : request.user.addr})
        return redirect('/user/login')

    def post(self, request):
        # checks which form data is being retrieved by form's keys
        if 'street' in request.POST.keys():
            form = AddrForm(request.POST)
            form.is_valid()
            request.user.addr.street_number = form.cleaned_data['street_number']
            request.user.addr.street = form.cleaned_data['street']
            request.user.addr.bloc = form.cleaned_data['bloc']
            request.user.addr.ap = form.cleaned_data['ap']
            request.user.addr.scara = form.cleaned_data['scara']
            request.user.addr.phone_number = form.cleaned_data['phone_number']    
            request.user.addr.save()
            request.user.save()
            return self.get(request)
        # form for name and password changing
        elif 'old_passwd' in request.POST.keys():
            form = ChangeForm(request.POST)
            if form.is_valid():
                # checks if the the password match otherwise returns an error message
                if not request.user.check_password(form.cleaned_data['old_passwd']):
                    return HttpResponse("Passwords do not match")
                if valid_pass(form.cleaned_data['passwd']):
                    # changes the user's password and reauthenticates the user back
                    obj = CustomUser.objects.get(email = request.user.email)
                    request.user.set_password(form.cleaned_data['passwd'])
                    request.user.save()
                    obj = authenticate(request, email = obj.email, password = form.cleaned_data['passwd'])
                    login(request, obj)
                if valid_name(form.cleaned_data['nume']):
                    # changes the user's name
                    request.user.nume = form.cleaned_data['nume']
                    request.user.save()
            addr = request.user.addr
            return render(request, 'extend_user.html', {'user': request.user, 'form' : form, 'addr' : addr})


class UserViewWish(View):
    '''
    Returns the user s wish list and wish products
    '''
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'wish_list.html', {'user': request.user, 'cos': WishList.objects.filter(email = request.user.email)})
        else:
            return redirect('/user/login')


class UserViewCart(View):
    '''
    Returns the cart products of the user
    '''
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'cart.html', {'user': request.user,  'cos': Cart.objects.filter(email = request.user.email),'len':len(Cart.objects.filter(email = request.user.email)),  'price' : Cart.get_total(request.user.email), 'checkout_ok': check_addr(request.user.addr)})
        return redirect("/user/login")
        

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
            adr = Address.objects.create(street = "", phone_number = "", scara = "")
            us = User.objects.create_user(email = form.cleaned_data['email'], addr = adr, password = form.cleaned_data['password'], nume=form.cleaned_data['nume'])
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
            # authenticates the user and creates a session
            user = authenticate(request, email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)    
                return redirect('/')
            else:
                return HttpResponse("No existing account with this credentials")
        else:
            form = LoginForm()
            return render(request, 'registration/login.html', {'form': form})
class LogoutView(View):
    def get(self, request):
        # logs out the user
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')

def checkout(request):
    '''
    Tries to send an email with the information about the products to the admin
    '''
    try:
        cart = Cart.objects.filter(nume = request.user.nume)
        email(request.user.nume, cart, request.user.addr)
        return redirect('/user/confirmation')
    except Exception as e:
        return HttpResponse(str(e))
    
    
def confirmation_show(request):
    return render(request, 'confirmaion_page.html', {})
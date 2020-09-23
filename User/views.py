from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required

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
            return render(request, 'extend_user.html', {'user': request.user, 'form': form, 'addr': request.user.addr})
        return redirect('/accounts/login')

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
            return render(request, 'wish_list.html', {'user': request.user, 'cos': WishList.objects.filter(email=request.user.email)})
        return redirect('/accounts/login')


class UserViewCart(View):
    '''
    Returns the cart products of the user
    '''
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'cart.html', {'user': request.user,  'cos': Cart.objects.filter(email=request.user.email),'len': len(Cart.objects.filter(email=request.user.email)),  'price' : Cart.get_total(request.user.email), 'checkout_ok': check_addr(request.user.addr) and len(Cart.objects.filter(email=request.user.email)) > 0})
        return redirect("/accounts/login")

class LogoutView(View):
    def get(self, request):
        # logs out the user
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')

@login_required
def checkout_from_cart(request):
    try:
        cart = Cart.objects.filter(email=request.user.email)
        email_cart_products(request.user, cart)
        cart.delete()
        return redirect('/user/confirmation')
    except Exception as e:
        return HttpResponse(str(e))

@login_required
def confirmation_show(request):
    return render(request, 'confirmaion_page.html', {})
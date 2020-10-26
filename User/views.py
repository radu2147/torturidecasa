from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from Cart.models import *
from .utils import *


# Create your views here.
class UserView(View):
    """
    Returns the user's page if the user is logged in else redirects to the login page
    """

    def get(self, request):
        form = AddrForm()
        if request.user.is_authenticated:
            return render(request, 'extend_user.html', {'user': request.user, 'form': form, 'addr': request.user.addr})
        return redirect('/accounts/login')

    def change_user_address(self, user, data):
        """
        Changes the user's address fields
        """
        user.addr.street_number = data['street_number']
        user.addr.street = data['street']
        user.addr.bloc = data['bloc']
        user.addr.ap = data['ap']
        user.addr.scara = data['scara']
        user.addr.phone_number = data['phone_number']
        user.addr.save()
        user.save()

    def change_user_data(self, request, data):
        """
        Updates the user fields with the user data
        If it works it doesn't return anything
        HttpResponse if the current password is not correct
        """
        # checks if the the password match otherwise returns an error message
        if not request.user.check_password(data['old_passwd']):
            return HttpResponse("Passwords do not match")
        if valid_pass(data['passwd']):
            # changes the user's password and reauthenticates the user back
            obj = CustomUser.objects.get(email=request.user.email)
            request.user.set_password(data['passwd'])
            request.user.save()
            obj = authenticate(request, email=obj.email, password=data['passwd'])
            login(request, obj)
        if valid_name(data['nume']):
            # changes the user's name
            request.user.nume = data['nume']
            request.user.save()

    def is_user_data_form(self, request):
        return 'street' in request.POST.keys()

    def is_user_addr_form(self, request):
        return 'street' in request.POST.keys()

    def post(self, request):
        # checks which form data is being retrieved by form's keys
        if self.is_user_addr_form(request):
            form = AddrForm(request.POST)
            form.is_valid()
            self.change_user_address(request.user, form.cleaned_data)
            return self.get(request)
        # form for name and password changing
        elif self.is_user_data_form(request):
            form = ChangeForm(request.POST)
            if form.is_valid():
                self.change_user_data(request, form.cleaned_data)
            addr = request.user.addr
            return render(request, 'extend_user.html', {'user': request.user, 'form': form, 'addr': addr})
        return None


class UserViewWish(View):
    """
    Returns the user s wish list and wish products
    """

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'wish_list.html',
                          {'user': request.user, 'cos': WishList.objects.filter(email=request.user.email)})
        return redirect('/accounts/login')


class UserViewCart(View):
    """
    Returns the cart products of the user
    """

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'cart.html',
                          {'user': request.user, 'cos': Cart.objects.filter(email=request.user.email),
                           'len': len(Cart.objects.filter(email=request.user.email)),
                           'price': Cart.get_total(request.user.email),
                           'checkout_ok': check_addr(request.user.addr) and len(
                               Cart.objects.filter(email=request.user.email)) > 0})
        return redirect("/accounts/login")


class LogoutView(View):
    """
    Logs out the active user if authenticated else returns the homepage
    """

    def get(self, request):
        # logs out the user
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')


@login_required
def checkout_from_cart(request):
    """
    Function that handles the checkout from cart.
    Login is required for this operation
    Sends the email order details and clears the existing cart.
    If the sent email raises an error the program will do the same

    """
    try:
        cart = Cart.objects.filter(email=request.user.email)
        email_cart_products(request.user, cart)
        cart.delete()
        return redirect('/user/confirmation')
    except Exception as e:
        return HttpResponse(str(e))


@login_required
def confirmation_show(request):
    """
    Shows a page with a confirmation message
    """
    return render(request, 'confirmaion_page.html', {})

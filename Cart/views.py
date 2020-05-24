from django.shortcuts import redirect
from .models import *
from HomePage.models import Produs
from django.http.response import HttpResponse

# Create your views here.

def add_to_cart(request, ident, gr, inscr):
    if request.user.is_authenticated:
        pr = Produs.objects.get(ident = ident)
        c, created = Cart.objects.get_or_create(email = request.user.email, prod_id = ident, nume = pr.nume, pret = pr.pret, gram = gr, inscr = inscr)
        if created == False:
            c.quantity += 1
            c.save()
        return redirect('/user/myaccount/cart')
    else:
        return redirect('/user/login')
    
def add_to_wish(request, ident):
    if request.user.is_authenticated:
        pr = Produs.objects.get(ident = ident)
        c, created = WishList.objects.get_or_create(email = request.user.email, prod_id = ident, nume = pr.nume, pret = pr.pret)
        return redirect('/user/myaccount/wish')
    else:
        return redirect('/user/login')
    
def remove_from_cart(request, ident, gr, inscr):
    if request.user.is_authenticated:
        try:
            c = Cart.objects.get(email = request.user.email, prod_id = ident, gram = gr, inscr = inscr)
            c.delete()
        except:
            return HttpResponse("Error")
        return redirect('/user/myaccount/cart')
    else:
        return redirect('/user/login')
def remove_from_wish(request, ident):
    if request.user.is_authenticated:
        try:
            c = WishList.objects.get(email = request.user.email, prod_id = ident)
            c.delete()
        except:
            return HttpResponse("Error")
        return redirect('/user/myaccount/wish')
    else:
        return redirect('/user/login')    
    
def remove_one_from_cart(request, ident, gr, inscr):
    if request.user.is_authenticated:
        c = Cart.objects.get(email = request.user.email, prod_id = ident, gram = gr, inscr = inscr)
        if c.quantity == 1:
            c.delete()
        else:
            c.quantity -= 1
            c.save()
        return redirect('/user/myaccount/cart')
    else:
        return redirect('/user/login')
    
    
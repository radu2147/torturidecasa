from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from .models import *
from HomePage.models import Produs
from django.http.response import HttpResponse

# Create your views here.

@login_required
def add_to_cart(request, ident, gr, inscr, date):
    pr = Produs.objects.get(ident=ident)
    c, created = Cart.objects.get_or_create(email = request.user.email, prod_id = ident, date_of_order = date, nume = pr.nume, pret = pr.pret, gram = gr, inscr = inscr, img_url = pr.cake_image.url)
    if created == False:
        c.quantity += 1
        c.save()
    return redirect('/user/myaccount/cart')

@login_required 
def add_to_wish(request, ident):
    pr = Produs.objects.get(ident=ident)
    c, created = WishList.objects.get_or_create(email=request.user.email, prod_id=ident, nume=pr.nume, pret=pr.pret, img_url=pr.cake_image.url)
    return redirect('/user/myaccount/wish')
 
@login_required     
def remove_from_cart(request, ident, gr, inscr, date):
    try:
        c = Cart.objects.get(email=request.user.email, prod_id=ident, gram=gr, inscr=inscr, date_of_order=date)
        c.delete()
    except:
        return HttpResponse("Error")
    return redirect('/user/myaccount/cart')

@login_required
def remove_from_wish(request, ident):
    try:
        c = WishList.objects.get(email = request.user.email, prod_id = ident)
        c.delete()
    except:
        return HttpResponse("Error")
    return redirect('/user/myaccount/wish')
    
    
@login_required
def remove_one_from_cart(request, ident, gr, inscr, date):
    c = Cart.objects.get(email = request.user.email, prod_id = ident, gram = gr, inscr = inscr, date_of_order = date)
    if c.quantity == 1:
        c.delete()
    else:
        c.quantity -= 1
        c.save()
    return redirect('/user/myaccount/cart')
    
    
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from .models import *
from HomePage.models import Produs
from django.http.response import HttpResponse

# Create your views here.

@login_required
def add_to_cart(request, ident, gr, inscr, date):
    '''
    Function that handles the addition of a Cart object with given fields in the Cart database.
    Login is required for this operation
    It redirects to the cart page
    '''
    pr = Produs.objects.get(ident=ident)
    c, created = Cart.objects.get_or_create(email=request.user.email, prod_id=ident, date_of_order=date, nume=pr.nume, pret=pr.pret, gram=gr, inscr=inscr, img_url=pr.cake_image.url)
    if created == False:
        c.quantity += 1
        c.save()
    return redirect('/user/myaccount/cart')

@login_required 
def add_to_wish(request, ident):
    '''
    Function that handles the addition of a Wish List object with given fields in the Wish List database.
    Login is required for this operation
    It redirects to the wish list page
    '''
    pr = Produs.objects.get(ident=ident)
    c, created = WishList.objects.get_or_create(email=request.user.email, prod_id=ident, nume=pr.nume, pret=pr.pret, img_url=pr.cake_image.url)
    return redirect('/user/myaccount/wish')
 
@login_required     
def remove_from_cart(request, ident, gr, inscr, date):
    '''
    Function that removes the object from the cart db, no matter the quantity
    Login is required for this operation
    It redirects to the cart page
    '''
    try:
        c = Cart.objects.get(email=request.user.email, prod_id=ident, gram=gr, inscr=inscr, date_of_order=date)
        c.delete()
    except:
        return HttpResponse("Error")
    return redirect('/user/myaccount/cart')

@login_required
def remove_from_wish(request, ident):
    '''
        Function used to remove a Wish List object with given id from the Wish List database.
        Login is required for this operation
        It redirects to the wish list page
        '''
    try:
        c = WishList.objects.get(email = request.user.email, prod_id = ident)
        c.delete()
    except:
        return HttpResponse("Error")
    return redirect('/user/myaccount/wish')
    
    
@login_required
def remove_one_from_cart(request, ident, gr, inscr, date):
    '''
    Function that decreases the quantity of a cart object with given fields from the database.
    The object is not removed from the cart db, unless the quantity is 1
    Login is required for this operation
    It redirects to the cart page
    '''
    c = Cart.objects.get(email = request.user.email, prod_id = ident, gram = gr, inscr = inscr, date_of_order = date)
    if c.quantity == 1:
        c.delete()
    else:
        c.quantity -= 1
        c.save()
    return redirect('/user/myaccount/cart')
    
    
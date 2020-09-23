from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
# Create your views here.
from .forms import *
from .utils import *
from User.utils import check_addr


class Personalize(View):
    '''
    Returns the personalize page if the user is logged in else returns the login page
    '''
    def get(self, request):
        if request.user.is_authenticated:           
            form = FilterForm()
            # checks the validity of a user's address
            return render(request, 'index.html', {'form': form, 'user': request.user, 'checkout_ok': check_addr(request.user.addr)})
        else:
            return redirect("/accounts/login")
        
        
    def post(self, request):
        form = FilterForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.usr = request.user
            order.save()
            email(request.user, order)
            return redirect('/user/confirmation')
        else:
            return HttpResponse("Formular invalid")
from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime

from .models import Produs
from re import sub


from .forms import *
from django.utils import timezone

from .utils import *
from Cart.models import *
from Comm.models import *
from Comm.forms import *

from Cart.forms import Comanda
    
class HomeSimple(View):
    
    def get(self, request):
        return redirect('page/1')
    
class FilterView(View):
    form_class = FilterForm
    
    def get(self, request, nume, mini, maxi, page):
        lista = []
        for obj in Produs.objects.all():
                if edit_distance_text(nume.lower(), obj.nume.lower()) <= 1 and mini <= obj.pret and maxi >= obj.pret:
                    lista.append(obj)
        fav_list = sorted([obj for obj in Produs.objects.all()], key = lambda x: x.finalrating, reverse = True)[:3]
        form = self.form_class()
        return render(request, 'extend.html', {'lista': lista[((page-1)*3):(page*3)], 'favorites': fav_list, 'form': form, 'user': request.user, 'antepre': page-2, 'prev':page-1, 'curent': page, 'next': page + 1, 'last': len(lista)//3 + 1, 'pagination': False, 'nume': nume, 'mini': mini, 'maxi': maxi})
    def post(self, request, nume, mini, maxi, page):
        form = self.form_class(request.POST)
        if form.is_valid():
            #empty string case
            if form.cleaned_data['nume'] == '':
                form.cleaned_data['nume'] = 'a'
            return redirect('filter', nume = form.cleaned_data['nume'], mini = int(form.cleaned_data['minprice']), maxi = int(form.cleaned_data['maxprice']), page = 1)
        else:
            return redirect("/")
        
class ProductView(View):
    form_class = FilterForm
    
    def get(self, request, page):
        # for sorting purpose
        lista = [obj for obj in Produs.objects.all()]
        fav_list = sorted(lista, key = lambda x: x.finalrating, reverse = True)[:3]
        if request.user.is_authenticated:
            for el in lista:
                try:
                    p = WishList.objects.get(email = request.user.email, prod_id = el.ident)
                    el.wish = True
                except:
                    pass
        form = self.form_class()
        
        return render(request, 'extend.html', {'lista': Produs.objects.all()[((page-1)*3):(page * 3)], 'favorites': fav_list, 'form': form, 'user':request.user, 'prev': page - 1,  'curent': page, 'next': (page + 1), 'last': (len(lista)//3 + 1), 'antepen': page-2, 'pagination': True})
    
    def post(self, request, page):
        form = self.form_class(request.POST)
        if form.is_valid():
            #empty string case
            if form.cleaned_data['nume'] == '':
                form.cleaned_data['nume'] = 'a'
            return redirect('filter', nume = form.cleaned_data['nume'], mini = int(form.cleaned_data['minprice']), maxi = int(form.cleaned_data['maxprice']), page = 1)
        else:
            return self.get(request, page)
        
class ProductPage(View):
    
    def get(self, request, ident):
        obj = Produs.objects.get(ident=ident)
        url_img = obj.image.url
        lista = Comment.objects.filter(produs = obj)
        nr = int(obj.finalrating)
        return render(request, 'produs.html', {'url_img': url_img,'user': request.user, 'obj': obj, 'comms': lista, 'times': [0 for i in range(nr)]})
    
    def post(self, request, ident):
        if "rating" in request.POST.keys():
            form = FormComm(request.POST)
            if form.is_valid():
                if request.user.is_authenticated == False:
                    return redirect('/user/login')
                else:
                    prd = Produs.objects.get(ident = ident)
                    url_img = prd.image.url
                    comm, created = Comment.objects.get_or_create(user = request.user, produs = prd)
                    
                    if created == True:
                        prd.number += 1
                        prd.sum += form.cleaned_data['rating']
                    else:
                        prd.sum += form.cleaned_data['rating'] - comm.rating 
                    comm.text = form.cleaned_data['text']
                    comm.date = timezone.now()
                    comm.rating = form.cleaned_data['rating']
                    prd.finalrating = prd.sum / prd.number
                    prd.save()
                    comm.save()
                    nr = int(prd.finalrating)
                    lista = Comment.objects.filter(produs = prd)
                    return render(request, 'produs.html', {'url_img': url_img, 'user': request.user, 'obj': prd, 'comms': lista, 'times': [0 for i in range(nr)]})
        
            else:
                self.get(request, ident)
        elif "gramaj" in request.POST.keys():
            form = Comanda(request.POST)
            if form.is_valid():
                if request.user.is_authenticated == False:
                    return redirect('/user/login')
                else:
                    string = sub("\s", "_", form.cleaned_data['inscriptie'])
                    return redirect("Cart:add", ident = ident, gr = form.cleaned_data['gramaj'], inscr = string)
            else:
                self.get(request, ident)

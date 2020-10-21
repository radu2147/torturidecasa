from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from re import sub

from .forms import *

from .utils import *
from Cart.models import *
from Comm.models import *
from Comm.forms import *

from Cart.forms import Comanda


class HomeSimple(View):

    def get(self, request):
        return redirect('page/1')


class FilterView(View):
    '''
    The view that handles the page for the filtering form
    '''
    form_class = FilterForm

    def create_filtered_list(self, nume, mini, maxi, page):
        '''
        Creates and returns the list of filtered products based on name, min and max price, and the navigation
        page
        If the page is wrong it throws a 404 response
        '''
        lista = []
        for obj in Produs.objects.all():
            if edit_distance_text(nume.lower(), obj.nume.lower()) <= 1 and mini <= obj.pret and maxi >= obj.pret:
                lista.append(obj)
        if page > len(lista) // 3 + 1:
            return HttpResponse("404")
        lista.sort(key=lambda x: x.finalrating, reverse=True)
        return lista

    @staticmethod
    def create_top3_rated():
        '''
        Creates and return the top 3 Produss based on their final rating
        '''
        return sorted([obj for obj in Produs.objects.all()], key=lambda x: x.finalrating, reverse=True)[:3]

    def get(self, request, nume, mini, maxi, page):

        lista = self.create_filtered_list(nume, mini, maxi, page)
        fav_list = FilterView.create_top3_rated()
        form = self.form_class()
        return render(request, 'extend.html',
                      {'lista': lista[((page - 1) * 3):(page * 3)], 'favorites': fav_list, 'form': form,
                       'user': request.user, 'antepre': page - 2, 'prev': page - 1, 'curent': page, 'next': page + 1,
                       'last': (len(lista) - 1) // 3 + 1, 'pagination': False, 'nume': nume, 'mini': mini,
                       'maxi': maxi, 'is_filtered': True})

    def post(self, request, nume, mini, maxi, page):
        form = self.form_class(request.POST)
        if form.is_valid():
            # empty string case
            if form.cleaned_data['nume'] == '':
                form.cleaned_data['nume'] = 'a'
            return redirect('filter', nume=form.cleaned_data['nume'], mini=int(form.cleaned_data['minprice']),
                            maxi=int(form.cleaned_data['maxprice']), page=1)
        else:
            return redirect("/")


class ProductView(View):
    '''
    View that handles the logic of the home page
    '''
    form_class = FilterForm

    @staticmethod
    def create_top3_rated():
        '''
        Creates and return the top 3 Produss based on their final rating
        '''
        return sorted([obj for obj in Produs.objects.all()], key=lambda x: x.finalrating, reverse=True)[:3]

    def validate_pages_on_mainpage(self, page):
        if page > len(Produs.objects.all()) // 3 + 1:
            return HttpResponse("404")

    def get(self, request, page):
        self.validate_pages_on_mainpage(page)
        lista = [obj for obj in Produs.objects.all()]
        fav_list = ProductView.create_top3_rated()
        form = self.form_class()

        return render(request, 'extend.html',
                      {'lista': Produs.objects.all()[((page - 1) * 3):(page * 3)], 'favorites': fav_list, 'form': form,
                       'user': request.user, 'prev': page - 1, 'curent': page, 'next': (page + 1),
                       'last': ((len(lista) - 1) // 3 + 1), 'antepen': page - 2, 'is_filtered': False})

    def post(self, request, page):
        form = self.form_class(request.POST)
        if form.is_valid():
            # empty string case
            if form.cleaned_data['nume'] == '':
                form.cleaned_data['nume'] = 'a'
            return redirect('filter', nume=form.cleaned_data['nume'], mini=int(form.cleaned_data['minprice']),
                            maxi=int(form.cleaned_data['maxprice']), page=1)
        else:
            return self.get(request, page)


class ProductPage(View):

    def get(self, request, ident):
        obj = Produs.objects.get(ident=ident)
        lista = Comment.objects.filter(produs=obj)
        nr = int(obj.finalrating)
        return render(request, 'product.html', {
                                               'user': request.user,
                                               'obj': obj,
                                               'comms': lista,
                                               'times': [0 for _ in range(nr)]})

    def update_comments(self, ident, user, data):
        prd = Produs.objects.get(ident=ident)
        try:
            comm = Comment.objects.get(user=user, produs=prd)
            prd.sum += data['rating'] - comm.rating
            comm.text = data['text']
            comm.date = timezone.now()
            comm.rating = data['rating']
            comm.save()

        except:
            com = Comment.objects.create(user=user, produs=prd, text=data['text'],
                                         date=timezone.now(), rating=data['rating'])
            com.save()
            prd.number += 1
            prd.sum += data['rating']

        prd.finalrating = prd.sum / prd.number
        prd.save()
        return prd

    def post(self, request, ident):
        if "rating" in request.POST.keys():

            form = FormComm(request.POST)
            if form.is_valid():
                if not request.user.is_authenticated:
                    return redirect('/accounts/login')
                else:
                    prd = self.update_comments(ident, request.user, form.cleaned_data)
                    nr = int(prd.finalrating)
                    lista = Comment.objects.filter(produs=prd)
                    return render(request, 'product.html',
                                  {'user': request.user, 'obj': prd, 'comms': lista,
                                       'times': [0 for _ in range(nr)]})
            else:
                return self.get(request, ident)
        elif "gramaj" in request.POST.keys():
            form = Comanda(request.POST)
            if form.is_valid():
                string = sub("\s", "_", form.cleaned_data['inscriptie'])
                return redirect("Cart:add", ident=ident, gr=form.cleaned_data['gramaj'], inscr=string,
                                        date=form.cleaned_data['date_of_order'])
            else:
                return self.get(request, ident)

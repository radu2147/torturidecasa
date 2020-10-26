from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from re import sub

from .forms import *
from .utils import *

from Comm.models import *
from Comm.forms import *

from Cart.forms import Comanda


class HomeSimple(View):

    def get(self, request):
        return redirect('page/1')


class FilterView(View):
    """
    The view that handles the page with filtered products
    """
    form_class = FilterForm

    def create_filtered_list(self, nume, mini, maxi, page):
        """
        Creates and returns the list of filtered products based on name, min and max price, and the navigation
        page with validation of the fields
        If the page is wrong it throws a 404 response
        """
        lista = []
        for obj in Produs.objects.all():
            if edit_distance_text(nume.lower(), obj.nume.lower()) <= 1 and mini <= obj.pret <= maxi:
                lista.append(obj)
        if page > len(lista) // 3 + 1:
            return HttpResponse("404")
        lista.sort(key=lambda x: x.finalrating, reverse=True)
        return lista

    @staticmethod
    def create_top3_rated():
        """
        Creates and return the top 3 Produss based on their final rating
        """
        return sorted([obj for obj in Produs.objects.all()], key=lambda x: x.finalrating, reverse=True)[:3]

    def get(self, request, nume, mini, maxi, page):
        """
        Method that handles the get request on a page with filtered products
        """
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
    """
    View that handles the logic of the home page
    """
    form_class = FilterForm

    @staticmethod
    def create_top3_rated():
        """
        Creates and return the top 3 Produss based on their final rating
        """
        return sorted([obj for obj in Produs.objects.all()], key=lambda x: x.finalrating, reverse=True)[:3]

    def validate_pages_on_mainpage(self, page):
        """
        Checks if the requested page is within the bounds of the number of objects.
        Output: Exception if the page requested is invalid
        """
        if page > len(Produs.objects.all()) // 3 + 1:
            return HttpResponse("404")

    def get(self, request, page):
        """
        Method that handles the get request of main page
        """
        self.validate_pages_on_mainpage(page)
        lista = [obj for obj in Produs.objects.all()]
        fav_list = ProductView.create_top3_rated()
        form = self.form_class()

        return render(request, 'extend.html',
                      {'lista': Produs.objects.all()[((page - 1) * 3):(page * 3)],
                       'favorites': fav_list,
                       'form': form,
                       'user': request.user,
                       'prev': page - 1,
                       'curent': page,
                       'next': (page + 1),
                       'last': ((len(lista) - 1) // 3 + 1),
                       'antepen': page - 2,
                       'is_filtered': False})

    def post(self, request, page):
        """
            Method that handles the post request of main page
        """
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
        """
        Method that handles the get request of a product's page
        """
        obj = Produs.objects.get(ident=ident)
        lista = Comment.objects.filter(produs=obj)
        nr = int(obj.finalrating)
        return render(request, 'product.html', {
                                               'user': request.user,
                                               'obj': obj,
                                               'comms': lista,
                                               'times': [0 for _ in range(nr)]})

    def update_comments(self, ident, user, data):
        """
        This method updates the comment text if it already exists.
        Otherwise it creates the comments with the given parameters
        The method updates the product's rating sum, and final rating
        Output:
        Returns the updated product.
        """
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

    def isCommForm(self, request):
        """
        Check if the submitted form is the comments form
        """
        return 'rating' in request.POST.keys()

    def isOrderForm(self, request):
        """
        Check if the form submitted is the order form
        """
        return 'gramaj' in request.POST.keys()

    def format_inscriptie(self, string):
        """
        formats the string s to replace the whitespaces (' ') with underscore character ('_')
        returns the formatted string
        """
        return sub("\s", "_", string)

    def check_user_authenticated(self,user):
        """
        Checks if current session's user is authenticated
        Redirects to the login page if anonymous user
        """
        if not user.is_authenticated:
            return redirect('/accounts/login')

    def post(self, request, ident):
        """
        Method that handles the post request of the view
        """
        if self.isCommForm(request):

            form = FormComm(request.POST)
            if form.is_valid():
                self.check_user_authenticated(request.user)
                # the product with updated comments
                prd = self.update_comments(ident, request.user, form.cleaned_data)
                nr = int(prd.finalrating)
                lista = Comment.objects.filter(produs=prd)
                return render(request, 'product.html', {'user': request.user,
                                                        'obj': prd,
                                                        'comms': lista,
                                                        'times': [0 for _ in range(nr)]})
            return self.get(request, ident)
        elif self.isOrderForm(request):
            form = Comanda(request.POST)
            if form.is_valid():
                string = self.format_inscriptie(form.cleaned_data['inscriptie'])
                return redirect("Cart:add",
                                ident=ident,
                                gr=form.cleaned_data['gramaj'],
                                inscr=string,
                                date=form.cleaned_data['date_of_order'])
            return self.get(request, ident)
        return None

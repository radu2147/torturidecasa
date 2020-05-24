from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from .forms import *


class Personalize(View):
    def get(self, request):
        if request.user.is_authenticated:
            usr = request.user
            form = FilterForm()
            return render(request, 'index.html', {'form' : form, 'user': usr})
        else:
            return redirect("/user/login")
        
        
    def post(self, request):
        form = FilterForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit = False)
            order.usr = request.user
            order.save()
            return redirect("/")
        else:
            return self.get(request)
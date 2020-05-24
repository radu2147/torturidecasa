'''
Local urls file
'''
from django.urls import path
from . import views

urlpatterns = [
    path('clean/', views.corect, name = "clean"),
]

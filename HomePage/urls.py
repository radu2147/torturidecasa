'''
Local urls file
'''
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('page/<int:page>', views.ProductView.as_view(), name = 'Homepage'),
    path('filter/<slug:nume>/<int:mini>/<int:maxi>/page/<int:page>', views.FilterView.as_view(), name='filter'),
    path('product/<int:ident>', views.ProductPage.as_view(), name="Prod"),
    path('', views.HomeSimple.as_view(), name = 'home'),
]
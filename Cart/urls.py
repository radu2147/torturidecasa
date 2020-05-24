'''
Local urls file
'''
from django.urls import path
from . import views

app_name="<Cart>"

urlpatterns = [
    path('add-to-cart/<int:ident>/<int:gr>/<slug:inscr>', views.add_to_cart, name = 'add'),
    path('delete-from-cart/<int:ident>/<int:gr>/<slug:inscr>', views.remove_from_cart, name = 'del'),
    path('delete-one-from-cart/<int:ident>/<int:gr>/<slug:inscr>', views.remove_one_from_cart, name = 'del_one'),
    path('add-to-wish/<int:ident>', views.add_to_wish, name = 'add_wish'),
    path('delete-from-wish/<int:ident>', views.remove_from_wish, name = 'del_wish'),
]
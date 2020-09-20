'''
Local urls file
'''
from django.urls import path
from . import views

urlpatterns = [
    path('myaccount/', views.UserView.as_view(), name="User"),
    path('myaccount/wish', views.UserViewWish.as_view(), name="wish"),
    path('myaccount/cart', views.UserViewCart.as_view(), name="cart"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('confirmation/', views.confirmation_show),
    path('checkout_form_cart', views.checkout_from_cart, name="checkout_from_cart")
]

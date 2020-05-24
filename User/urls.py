'''
Local urls file
'''
from django.urls import path
from . import views

urlpatterns = [
    path('myaccount/', views.UserView.as_view(), name = "User"),
    path('myaccount/wish', views.UserViewWish.as_view(), name = "wish"),
    path('myaccount/cart', views.UserViewCart.as_view(), name = "cart"),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view(), name = "login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]

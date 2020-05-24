'''
Local urls file
'''
from django.urls import path
from . import views

app_name="<Cart>"

urlpatterns = [
    path('add-comm/<int:ident>', views.add_comm, name = 'add_comm'),
    
]
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
    
from .managers import CustomUserManager
from HomePage.models import Produs

from .validators import *
    
   
class Address(models.Model):
	street = models.CharField(max_length = 100)
	phone_number = models.CharField(max_length = 10, validators=[phone])
	street_number = models.IntegerField(validators=[poz])
	bloc = models.IntegerField(validators=[poz])
	scara = models.CharField(validators=[scara], max_length = 1)
	ap = models.IntegerField(validators=[poz])
    
class CustomUser(AbstractUser):
    
    email = models.EmailField(_('email address'), unique=True)
    nume = models.CharField(max_length = 50, default='bla', blank = True)
    username = models.CharField(default = "", max_length = 50, blank = True)
    addr = models.ForeignKey(Address, related_name = "address_user", on_delete = models.CASCADE)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.nume




    

    
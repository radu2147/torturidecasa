from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
    
from .managers import CustomUserManager
from HomePage.models import Produs

from .validators import *
    
    
    
class CustomUser(AbstractUser):
    
    email = models.EmailField(_('email address'), unique=True)
    nume = models.CharField(max_length = 50, default='bla', blank = True)
    username = models.CharField(default = "", max_length = 50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.nume

class Address(models.Model):
	street = models.CharField(max_length = 100)
	street_number = models.IntegerField(validators=[phone, poz])
	bloc = models.IntegerField(validators=[poz])
	scara = models.IntegerField(validators=[scara])
	ap = models.IntegerField(validators=[poz])

    

    
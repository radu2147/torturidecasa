from django.db import models
from django.utils import timezone
from HomePage.models import Produs
from User.models import *

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, related_name = "user", on_delete=models.CASCADE)
    produs = models.ForeignKey(Produs, related_name="produs", on_delete=models.CASCADE)
    date = models.DateField(default = timezone.now())
    rating = models.IntegerField(default = 1)
    text = models.TextField(default = "", blank = True)
    
    def __str__(self):
        return "Comm: " + self.produs.nume + " " + str(self.rating)

from django.db import models
from HomePage.models import Produs
# Create your models here.

class ProdUserRel(models.Model):
    email = models.EmailField()
    prod_id = models.IntegerField()

    
    def __str__(self):
        return self.email + str(self.prod_id)

class Cart(ProdUserRel):
    quantity = models.IntegerField(default = 1)
    nume = models.CharField(max_length = 50, default = "")
    pret = models.FloatField(default = 0)
    gram = models.IntegerField(default = 0)
    inscr = models.CharField(max_length = 30, default = "")
    
    def get_subtotal(self):
        return (self.pret * self.quantity * 100) // 1 / 100
    
    @staticmethod
    def get_total(email):
        price = 0
        for el in Cart.objects.filter(email = email):
            price += el.get_subtotal()
        return (price * 100) // 1 / 100
    
class WishList(ProdUserRel):
    pret = models.FloatField()
    nume = models.CharField(max_length = 50)
    

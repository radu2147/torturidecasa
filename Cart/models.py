from django.db import models
from HomePage.models import Produs
# Create your models here.

class ProdUserRel(models.Model):
    email = models.EmailField()
    prod_id = models.IntegerField()

    
    def __str__(self):
        return self.email + str(self.prod_id)

class Cart(ProdUserRel):
    quantity = models.IntegerField(default=1)
    nume = models.CharField(max_length=50, default="")
    pret = models.FloatField(default=0)
    gram = models.IntegerField(default=0)
    inscr = models.CharField(max_length=30, default="")
    img_url = models.CharField(max_length=100, null=True, blank=True)
    date_of_order = models.DateField()
    
    def get_subtotal(self):
        return (self.pret * self.quantity * self.gram * 100) // 1 / 100

    def get_inscr(self):
        return " ".join(self.inscr.split('_'))

    def get_measuring_unit(self):
        return Produs.objects.get(ident=self.prod_id).measure_unit
    
    @staticmethod
    def get_total(email):
        price = 0
        for el in Cart.objects.filter(email=email):
            price += el.get_subtotal()
        return (price * 100) // 1 / 100


class WishList(ProdUserRel):

    pret = models.FloatField()
    nume = models.CharField(max_length=50)
    img_url = models.CharField(max_length=100, null=True, blank=True)

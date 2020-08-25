from django.db import models

# Create your models here.
class Produs(models.Model):
    """
    Atributele produsului
    """
    ident = models.IntegerField(unique=True)
    nume = models.CharField(max_length=50)
    pret = models.FloatField()
    descr = models.TextField()
    sum = models.IntegerField(default=0, editable=False)
    number = models.IntegerField(default=0, editable=False)
    finalrating = models.FloatField(default=0, editable=False)
    image = models.ImageField(blank=True, null=True, upload_to='products/img/')
    measure_unit = models.CharField(default='kg', max_length=5)
    
    def show_rating(self):
        return self.finalrating * 100 // 1 / 100
    
    def __str__(self):
        return self.nume
    
    def __eq__(self, ot):
        return self.nume == ot.nume

        



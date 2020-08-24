from django.db import models
from .validators import valid_date
from User.models import CustomUser

# Create your models here.
class CustomOrder(models.Model):
    tort = models.ImageField(upload_to='products/custom/', null=True, blank=True)
    description = models.TextField(default="")
    quantity = models.IntegerField(default=1)
    date = models.DateField(validators=[valid_date])
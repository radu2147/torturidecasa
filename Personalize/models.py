from django.db import models
from .validators import valid_date
from cloudinary.models import CloudinaryField

# Create your models here.
class CustomOrder(models.Model):
    image = CloudinaryField('image')
    description = models.TextField(default="")
    quantity = models.IntegerField(default=1)
    date = models.DateField(validators=[valid_date])
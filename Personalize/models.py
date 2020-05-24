from django.db import models
from User.models import CustomUser

# Create your models here.
class CustomOrder(models.Model):
    tort = models.ImageField(blank = True, null = True, upload_to = 'products/custom/')
    fig = models.BooleanField()
    usr = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    
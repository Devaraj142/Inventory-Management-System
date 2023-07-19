from django.db import models
from datetime import datetime
# Create your models here.

class Addproduct(models.Model):
    pname = models.CharField(max_length=50)
    name  = models.CharField(max_length=50)
    place = models.CharField(max_length=50)

class Addmove(models.Model):
    mpname = models.CharField(max_length=50)
    orgin = models.CharField(max_length=50)
    destiny = models.CharField(max_length=50)
    qty = models.IntegerField()


 



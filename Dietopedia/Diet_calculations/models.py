from django.db import models
from Login.models import Customers
from django.contrib.auth.models import User,auth

# Create your models here.

class CalculationsBMI(models.Model):
    BMR=models.FloatField()
    date=models.DateTimeField(auto_now_add=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

class CalculationsBDI(models.Model):
    BDI=models.FloatField()
    date=models.DateTimeField(auto_now_add=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
   
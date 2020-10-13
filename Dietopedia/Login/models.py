from django.db import models
from django import forms

# Create your models here.
class Customers(models.Model):
    First_Name= models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Age=models.IntegerField()
    Email= models.EmailField(max_length=70,blank=False , unique= True)
    Password=models.CharField(max_length=20,blank=False,default="hello")
    ConfirmPassword=models.CharField(max_length=20,blank=False,default="hello")
    ProfilePic=models.ImageField(blank=True,null=True)


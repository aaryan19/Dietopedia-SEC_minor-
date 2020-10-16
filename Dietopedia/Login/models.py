from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    Gender=models.CharField(max_length=20)
    Age=models.IntegerField()
    Calories=models.IntegerField(default=1200)
    Email= models.EmailField(max_length=70,blank=False , unique= True,default="test@gmail.com")
    Address=models.CharField(max_length=30,default='Nepal',)
    ProfilePic=models.ImageField(blank=True,null=True)


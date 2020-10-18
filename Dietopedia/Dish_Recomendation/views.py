from django.shortcuts import render,redirect
from . import test_api2
from django.contrib import auth
# Create your views here.

def Recommend(request):
    name=test_api2.itemname
    cal=test_api2.calories
    fat=test_api2.fat
    serving=test_api2.serving
  
    return render(request,"Dish_rec.html",{"name":name ,"cal":cal,"fat":fat,"serving":serving})

def Logout(request):
    auth.logout(request)
    return redirect("/")
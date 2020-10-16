from django.shortcuts import render
from . import test_api
# Create your views here.

def Recommend(request):
    name=test_api.name
    image=test_api.image
    energy=test_api.energy
    protien=test_api.protien
    fat=test_api.fat
    category=test_api.category
    ingredients=test_api.ingredients
    return render(request,"Dish_rec.html",{"name":name ,"image":image,"energy":energy,"protien":protien})


from django.shortcuts import render

# Create your views here.

def Recommend(request):
    return render(request,"Dish_rec.html",{})


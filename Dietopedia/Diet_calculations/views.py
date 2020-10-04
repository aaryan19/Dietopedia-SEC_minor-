from django.shortcuts import render

# Create your views here.
def BMI(request):
    return render(request,"Diet_calculations/BMI.html",{})
    
def BDI(request):
    return render(request,"Diet_calculations/BDI.html",{})

def Profile(request):
    return render(request,"Diet_calculations/Profile.html",{})

def History(request):
    return render(request,"Diet_calculations/History.html",{})


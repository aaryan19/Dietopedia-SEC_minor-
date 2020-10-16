from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='../log/signin')
def BMI(request):
    return render(request,"Diet_calculations/BMI.html",{})
@login_required(login_url='../log/signin')    
def BDI(request):
    return render(request,"Diet_calculations/BDI.html",{})
@login_required(login_url='../log/signin')
def Profile(request):
    return render(request,"Diet_calculations/Profile.html",{})
@login_required(login_url='../log/signin')
def History(request):
    return render(request,"Diet_calculations/History.html",{})

def Logout(request):
    auth.logout(request)
    return redirect("/")
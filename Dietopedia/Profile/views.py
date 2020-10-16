from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.
@login_required(login_url='../log/signin')
def Profile(request):
    return render(request,"Profile.html")
def Logout(request):
    auth.logout(request)
    return redirect("/")
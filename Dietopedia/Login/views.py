from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Customers
# Create your views here.

def SignUp(request):

    if  request.method== 'POST':
        Username= request.POST["uname"]
        First_Name=request.POST["fname"]
        Email= request.POST["email"]
        Password=request.POST["password"]
        CPassword=request.POST["cpassword"]
        Gender=request.POST["gender"]
        Age=request.POST["age"]
        
        if Password==CPassword:
            user=User.objects.create_user(username=Username,first_name=First_Name,password=Password,email=Email)
            user.save()   
            newextended= Customers(Gender=Gender,Age=Age,user=user)
            newextended.save()
            print("User Created")
           
            return(redirect('/log/signin/'))
        else:
            messages.info(request,"Password not matching")
            return(redirect('/log/signup/'))
    else:
       return render(request,"signup.html",{})


def SignIn(request):
        if request.method == "POST":
            username=request.POST['Username']
            password=request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return (redirect('/profile/'))
            else:
                messages.info(request,"Invalid Credentials")
                return (redirect('/log/signin'))
        else:
         return render(request,"signin.html",{})    

def Logout(request):
    auth.logout(request)
    return redirect("/")
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import CalculationsBMI,CalculationsBDI
from django.contrib.auth.models import User
from Login.models import Customers


# Create your views here.
@login_required(login_url='../log/signin')
def BMR(request):
     if  request.method== 'POST':
        height =request.POST['height']
        weight=request.POST['weight']
        user=request.user
        age =request.POST['age']
        Gender=request.POST['gender']
        exer =request.POST['exercise']
        if height =='' :
            print(age)
            if weight =='':
                if age =='':
                 return render(request,"Diet_calculations/BMR.html")
        else:
            if Gender == '1' :
                bmr = 66 + ( 6.23 * float(weight)) + ( 12.7 *float(height)  ) - ( 6.8 * float(age)  )
                if (exer == '1'):
                    bdiwithexercise= bmr*1.2
                            
                elif (exer == '2'):
                    bdiwithexercise= bmr*1.375
                            
                elif (exer == '3'):
                    bdiwithexercise= bmr*1.55
                            
                elif (exer == '4'):
                    bdiwithexercise= bmr*1.725
                            
                elif (exer == '5'):
                    bdiwithexercise= bmr*1.9
                
                user=request.user
                addbdio= CalculationsBMI(user=user,BMR=bdiwithexercise)
                addbdio.save()
                return render(request,"Diet_calculations/BMR.html")
            else:
                bmr =655 + ( 4.35 * float(weight)) + ( 4.7 * float(height) ) - ( 4.7 * float(age))
                if (exer== '1'):
                    bdiwithexercise= bmr*1.2
                            
                elif (exer== '2'):
                    bdiwithexercise= bmr*1.375
                            
                elif (exer== '3'):
                    bdiwithexercise= bmr*1.55
                            
                elif (exer== '4'):
                    bdiwithexercise= bmr*1.725
                            
                elif (exer== '5'):
                    bdiwithexercise= bmr*1.9
                
                user=request.user 
                test=CalculationsBMI.objects.filter(user=user).last()
                user=request.user
                addbdio= CalculationsBMI(user=user,BMR=bdiwithexercise)
                addbdio.save() 
                return render(request,"Diet_calculations/BMR.html",{"test":test})
           

             
     else:
        user=request.user 
        test=CalculationsBMI.objects.filter(user=user).last()
        return render(request,"Diet_calculations/BMR.html",{"test":test})

         
    
@login_required(login_url='../log/signin')    
def BDI(request):
    return render(request,"Diet_calculations/BDI.html")
    

    


@login_required(login_url='../log/signin')
def Profile(request):


    
    return render(request,"Diet_calculations/Profile.html",{})
@login_required(login_url='../log/signin')


def History(request):
    user=request.user
    all_bmr=CalculationsBMI.objects.filter(user=user)
    all_bdi=CalculationsBDI.objects.filter(user=user)
    return render(request,"Diet_calculations/History.html",{"bmi":all_bmr,"bdi":all_bdi})


def Logout(request):
    auth.logout(request)
    return redirect("/")
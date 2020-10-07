
from django.urls import path
from . import views

urlpatterns =[
    path('signup/',views.SignUp,name="SignUP"),
    path('signin/',views.SignIn,name="SignUP"),
]
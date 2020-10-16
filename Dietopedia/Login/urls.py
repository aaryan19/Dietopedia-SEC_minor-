
from django.urls import path
from . import views

urlpatterns =[
    path('signup/',views.SignUp,name="SignUP"),
    path('signin/',views.SignIn,name="SignIN"),
    path('Logout',views.Logout,name="Logout"),
]
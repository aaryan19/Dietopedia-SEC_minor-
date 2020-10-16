from django.urls import path
from . import views

urlpatterns =[
    path('BMI',views.BMI,name="BMI"),
    path('BDI',views.BDI,name="BDI"),
    path('History',views.History,name="History"),
    path('Logout',views.Logout,name="Logout")
]
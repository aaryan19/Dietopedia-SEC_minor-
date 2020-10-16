
from django.urls import path
from . import views

urlpatterns =[
    path('',views.Landing,name="Landing"),
  
]
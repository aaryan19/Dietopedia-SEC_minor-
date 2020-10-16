from django.urls import path
from . import views


urlpatterns =[
    path('Recomendation',views.Recommend,name="Dish Recommendation"),
  
]
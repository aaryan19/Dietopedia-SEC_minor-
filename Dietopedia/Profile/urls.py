
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =[
    path('',views.Profile,name="Profile"),
    path('Logout',views.Logout,name="Logout"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

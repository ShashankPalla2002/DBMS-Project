from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home),    
    path('crime_details/<str:title>', views.details),
=======
    path('', views.home),
    path('', views.crime_desc)    
>>>>>>> 3ee621634775f2a6040571cb374de2e964c1b0b2
]

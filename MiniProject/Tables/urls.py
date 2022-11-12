from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home),    
    path('crime_details/<str:title>', views.details),
<<<<<<< HEAD
=======
=======
    path('', views.home),
    path('', views.crime_desc)    
>>>>>>> 3ee621634775f2a6040571cb374de2e964c1b0b2
>>>>>>> e6e5626dfe20087ba2d5e5a9bc1735368e6a5f88
]

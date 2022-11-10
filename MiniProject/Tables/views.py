from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import IPC_Sections

def home(request):         
    return render (request, 'Tables/home.html')
    

    
    
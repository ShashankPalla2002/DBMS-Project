from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person_Related
from .models import Government_Related
from .models import Property_Related

def home(request):     
    persons = Person_Related.objects.all()
    government = Government_Related.objects.all()
    property = Property_Related.objects.all()

    return render (request, 'Tables/home.html', {'person' : persons, 'government' : government, 'property' : property})
    
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e6e5626dfe20087ba2d5e5a9bc1735368e6a5f88
def details(request,title):     
    print(title)
    t = Person_Related.objects.filter(pr_crime_title=title)
    print(t)
    return render(request, 'Tables/crime_details.html')
    
<<<<<<< HEAD
=======
=======
def crime_desc(request):
    return render (request)

>>>>>>> 3ee621634775f2a6040571cb374de2e964c1b0b2
>>>>>>> e6e5626dfe20087ba2d5e5a9bc1735368e6a5f88
    
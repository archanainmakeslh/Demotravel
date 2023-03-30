
from django.shortcuts import render
from . models import Place
from . models import Person

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    element = Person.objects.all()
    return render(request, "index.html", {'result': obj, 'individual': element})


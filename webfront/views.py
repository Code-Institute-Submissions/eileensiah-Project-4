from django.shortcuts import render, HttpResponse
from webfront.models import Maid

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, "index.html")
    
  
def searchmaid(request):
    searchmaid = Maid.objects.all()
    return render(request, "searchmaid.html")
    


def contactus(request):
    return render(request, "contactus.html")  
    
    
    
def shortlisted(request):
    return render(request, "shortlisted.html")  
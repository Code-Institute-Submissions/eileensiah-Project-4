from django.shortcuts import render, HttpResponse
from agency.models import Maid
from accounts.models import User
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.role == "Agency":
            return redirect("enquiry")
        else:
            return redirect("index")


def index(request):
    
    if request.method == 'POST':
        nationality = request.POST.get('nationality')
        type = request.POST.get('type')
        responsibility = request.POST.get('responsibility')
        return redirect('searchmaiddefine',nationality,type,responsibility)
    
        
    return render(request, "index.html")
    

 
def searchmaid(request):
    
    filter = request.GET;
    if len(filter) >0:
        searchmaid = Maid.objects.filter(**filter)
    else:
        searchmaid = Maid.objects.all()
    context = {
        "searchmaid": searchmaid
    }
    return render(request, "searchmaid.html" , context)
    


def contactus(request):
    return render(request, "contactus.html")  
    
    
    
def shortlisted(request):
    return render(request, "shortlisted.html")  
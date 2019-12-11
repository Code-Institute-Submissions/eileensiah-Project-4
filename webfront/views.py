from django.shortcuts import render, HttpResponse
from agency.models import Maid
from accounts.models import User, Employer
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from agency.models import Enquiry, Shortlist
from django.contrib import messages
from shortlisted_cart.models import ShortlistedMaid

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.role == "Agency":
            return redirect("enquiry")
        else:
            return redirect("index")


def index(request):
    
    return render(request, "index.html")
    

 
def searchmaid(request):
    
    filter = request.GET;
    results = {
        'nationality': filter.get("nationality"),
        'type_of_maid': filter.get('type_of_maid'),
        'main_responsibility': filter.get('main_responsibility'),
        'language_ability': filter.get('language_ability'),
        'marital_status': filter.get('marital_status'),
        'age': filter.get('age'),
    }
    print(results)
    if results["nationality"]== "none" or results['nationality']==None:
        del results["nationality"]
        
    if results["type_of_maid"]== "none" or results['type_of_maid']==None:
        del results["type_of_maid"]
        
    if results["main_responsibility"]== "none" or results['main_responsibility']==None:
        del results["main_responsibility"]
    
    if results["language_ability"]== "none" or results['language_ability']==None:
        del results["language_ability"]
        
    if results["marital_status"]== "none" or results['marital_status']==None:
        del results["marital_status"]
        
    if results["age"]== "none" or results['age']==None:
        del results["age"]
    
    if len(results) >0:
        print(results)
        searchmaid = Maid.objects.filter(**results)
      
    else:
        searchmaid = Maid.objects.all()
    context = {
        "searchmaid": searchmaid
    }
    return render(request, "searchmaid.html" , context)
    


def contactus(request):
    employer = None
    if request.user.is_authenticated and request.user.role == "Employer":
        employer = Employer.objects.get(user=request.user)
    if request.method == 'POST':
        enquiry= Enquiry()
        enquiry.name= request.POST.get('input_name')
        enquiry.phonenumber= request.POST.get('input_phonenumber')
        enquiry.email= request.POST.get('input_email')
        enquiry.nationality= request.POST.get('input_nationality')
        enquiry.main_responsibility= request.POST.get('input_responsibility')
        enquiry.type_of_maid= request.POST.get('input_type_of_maid')
        enquiry.age= request.POST.get('input_age')
        enquiry.message= request.POST.get('input_message')
        enquiry.save()
    return render(request, "contactus.html", {
        "employer": employer
    })  
    
    
    
def shortlisted(request):
    shortlisted_maids = None
    employer = None
    if request.user.is_authenticated and request.user.role == "Employer":
        employer = Employer.objects.get(user=request.user)
        shortlisted_maids = list(ShortlistedMaid.objects.filter(owner=employer))
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.role == "Employer":
            for shortlisted_maid in shortlisted_maids:
                shortlist= Shortlist()
                shortlist.employer = employer
                shortlist.maid = shortlisted_maid.maid
                shortlist.agency = shortlisted_maid.maid.agency_name
                shortlist.message= request.POST.get('input_message')
                shortlist.save()
        else:
            return redirect("login")
    return render(request, "shortlisted.html", {
        "employer": employer,
        "shortlisted_maids": shortlisted_maids
    })   
    
def login_required(request):
    return render(request,"loginrequired.html")
    
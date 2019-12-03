from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


# Create your views here.
def agency_detail(request):
    return render(request, "agency_detail.html")
    


def all_enquiry(request):
    return render(request, "all_enquiry.html")  
    
    
    
def all_maid(request):
    return render(request, "all_maid.html") 
    

def collection(request):
    return render(request, "collection.html")
    
    


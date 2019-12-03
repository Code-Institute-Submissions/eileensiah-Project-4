from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from product_cart.models import CartItem


# Create your views here.
def add_biodata(request):
    return render(request, "add_biodata.html")
    

def agency_cart(request):
    # reminder: request.user is the currently logged in user
    all_cart_items = CartItem.objects.filter(owner=request.user)
    return render(request, 'agency_cart.html',{
        'all_cart_items':all_cart_items
    }) 
    
    
def enquiry(request):
    return render(request, "enquiry.html") 
    

def maid_list(request):
    return render(request, "maid_list.html")
    
    
def product(request):
    return render(request, "product.html")

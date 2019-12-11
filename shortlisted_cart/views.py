from django.shortcuts import render, redirect,reverse
from .models import ShortlistedMaid
from agency.models import Maid
from accounts.models import Employer



def view_shortlisted_cart(request):
    # reminder: request.user is the currently logged in user
    all_shortlisted_maids = ShortlistedMaid.objects.filter(owner=request.user)
    return render(request, 'webfront/shortlisted.html',{
        'all_shortlisted_maids':all_shortlisted_maids
    })



def add_to_shortlisted_cart(request, maid_id):
    
    # determine which maid we have shortlisted
    maid = Maid.objects.get(id=maid_id)
    
    employer = Employer.objects.get(user=request.user)
    
    # if the maid already exists in the user's shortlisted cart
    existing_shortlisted_maid = ShortlistedMaid.objects.filter(owner=employer, maid=maid).first()
    
    # if the shortlisted maid does not exist, create a new one
    if existing_shortlisted_maid == None:
        new_shortlisted_maid = ShortlistedMaid()
        new_shortlisted_maid.maid = maid
        new_shortlisted_maid.owner = employer
        new_shortlisted_maid.quantity = 1
        new_shortlisted_maid.save()
    else:
        # increases its quantity
        existing_shortlisted_maid.quantity += 0
        existing_shortlisted_maid.save()
    return redirect(reverse('searchmaid'))
   
   
    
def remove_from_shortlisted_cart(request, shortlisted_cart_item_id):

    existing_shortlisted_maid = ShortlistedMaid.objects.get(id=shortlisted_cart_item_id)
    existing_shortlisted_maid.delete()
    return redirect(reverse('shortlisted'))

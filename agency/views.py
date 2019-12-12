from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from product_cart.models import CartItem
from django.db.models import Sum
from .models import Maid, Enquiry, Shortlist
from accounts.models import Agency, User
from django.contrib.auth.decorators import login_required
from accounts.decorators import agency_required
from django.utils.dateparse import parse_date


# Create your views here.
@login_required
@agency_required
def add_biodata(request):
    return render(request, "add_biodata.html")
    
@login_required
@agency_required
def agency_cart(request):
    # reminder: request.user is the currently logged in user
    agency = Agency.objects.get(user=request.user)
    all_cart_items = CartItem.objects.filter(owner=request.user)
    total_price = 0
    for item in all_cart_items:
        total_price += item.month*item.plan.price

    return render(request, 'agency_cart.html',{
        'all_cart_items':all_cart_items,
        'total_price': total_price,
        'agency': agency
    }) 
    
@login_required
@agency_required
def enquiry(request):
    agency = Agency.objects.get(user=request.user)
    enquirys = list(Enquiry.objects.all())
    enquirys.reverse()
    return render(request, "enquiry.html", {
        'enquirys': enquirys,
        'agency': agency
    }) 
    
@login_required
@agency_required
def shortlist_enquiry(request):
    agency = Agency.objects.get(user=request.user)
    shortlists = list(Shortlist.objects.filter(agency=agency.agency_name))
    print(shortlists)
    shortlists.reverse()
    return render(request, "enquiry_shortlist.html", {
        'shortlists': shortlists,
        'agency': agency
    }) 
    
@login_required
@agency_required
def maid_list(request):
    agency = Agency.objects.get(user=request.user)
    if request.method == 'POST':
        maid= Maid()
        maid.agency_user=agency
        maid.name= request.POST.get('name')
        maid.nationality= request.POST.get('nationality')
        maid.type_of_maid= request.POST.get('type_of_maid')
        maid.main_responsibility= request.POST.get('main_responsibility')
        maid.language_ability= request.POST.get('language_ability')
        maid.marital_status= request.POST.get('marital_status')
        maid.religion= request.POST.get('religion')
        maid.no_of_children= request.POST.get('no_of_children')
        maid.education_level= request.POST.get('education_level')
        maid.agency_name= request.POST.get('agency_name')
        maid.maid_photo= request.FILES['maid_photo']
        maid.salary= request.POST.get('salary')
        maid.date_of_birth = request.POST.get('date_of_birth')
        maid.employment_history= request.POST.get('employment_history')
        maid.age= request.POST.get('age')
        maid.save()
    agency_user = Agency.objects.get(user=request.user)
    all_maid= Maid.objects.filter(agency_name=agency_user.agency_name)
    context = {
        'all_maid': all_maid,
        'agency': agency
    }
    return render(request, "maid_list.html", context)
    
@login_required
@agency_required
def edit_biodata(request, maid_id):
    agency = Agency.objects.get(user=request.user)
    maid = Maid.objects.get(id=maid_id)
    if request.method == 'POST':
        maid.name= request.POST.get('name')
        maid.nationality= request.POST.get('nationality')
        maid.type_of_maid= request.POST.get('type_of_maid')
        maid.main_responsibility= request.POST.get('main_responsibility')
        maid.language_ability= request.POST.get('language_ability')
        maid.marital_status= request.POST.get('marital_status')
        maid.religion= request.POST.get('religion')
        maid.no_of_children= request.POST.get('no_of_children')
        maid.education_level= request.POST.get('education_level')
        maid.agency_name= request.POST.get('agency_name')
        if request.FILES.get('maid_photo', False):
            maid.maid_photo= request.FILES['maid_photo']
        maid.salary= request.POST.get('salary')
        maid.date_of_birth = request.POST.get('date_of_birth')
        maid.employment_history= request.POST.get('employment_history')
        maid.age= request.POST.get('age')
        maid.save()
        return redirect("maid_list")
    context = {
        'maid': maid,
        'agency': agency
    }
    return render(request, "edit_biodata.html", context)

@login_required
@agency_required
def delete_biodata(request, maid_id):
    maid = Maid.objects.get(id=maid_id)
    maid.delete()
    return redirect("maid_list") 
    
@login_required
@agency_required
def product(request):
    agency = Agency.objects.get(user=request.user)
    return render(request, "product.html", {
        'agency': agency
    })
from django.shortcuts import render,redirect,reverse
from .models import CartItem, SubPlan



def view_cart(request):
    # reminder: request.user is the currently logged in user
    all_cart_items = CartItem.objects.filter(owner=request.user)
    return render(request, 'agency/agency_cart.template.html',{
        'all_cart_items':all_cart_items
    })

def add_to_cart(request, product_id):
    
    # determine which product we are buying
    plan = SubPlan.objects.get(pk=product_id)
    
    # if the product already exists in the user's shopping cart
    existing_cart_item = CartItem.objects.filter(owner=request.user, plan=plan).first()
    
    # if the cart item does not exist, create a new one
    if existing_cart_item == None:
        new_cart_item = CartItem()
        new_cart_item.plan = plan
        new_cart_item.owner = request.user
        new_cart_item.month = 1
        new_cart_item.save()
    else:
        # increases its month
        existing_cart_item.month += 1
        existing_cart_item.save()
    return redirect(reverse('product'))


    
def remove_from_cart(request, cart_item_id):

    existing_cart_item = CartItem.objects.get(pk=cart_item_id)
    existing_cart_item.delete()
    return redirect(reverse('agency_cart'))
    
def add_month(request, cart_item_id):

    existing_cart_item = CartItem.objects.get(pk=cart_item_id)
    print (existing_cart_item.month)
    existing_cart_item.add_month()
    existing_cart_item.save()
    print (existing_cart_item.month)
    return redirect(reverse('agency_cart'))
    
def minus_month(request, cart_item_id):

    existing_cart_item = CartItem.objects.get(pk=cart_item_id)
    print (existing_cart_item.month)
    existing_cart_item.minus_month()
    existing_cart_item.save()
    return redirect(reverse('agency_cart'))
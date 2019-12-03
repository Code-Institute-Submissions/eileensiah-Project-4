from django.urls import path, include
from .views import add_to_shortlisted_cart, view_shortlisted_cart, remove_from_shortlisted_cart


urlpatterns = [
    path('add_to_shortlisted_cart/<maid_id>', add_to_shortlisted_cart, name='add_to_shortlisted_cart'),
    path('view', view_shortlisted_cart, name='view_shortlisted_cart'),
    path('remove_from_shortlisted_cart/<shortlisted_cart_item_id>', remove_from_shortlisted_cart, name='remove_from_shortlisted_cart')
   
]
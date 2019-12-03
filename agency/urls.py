from django.urls import path
from django.conf.urls import url
from .views import add_biodata, agency_cart, enquiry, maid_list, product


urlpatterns = [
    path('', enquiry, name="enquiry"),
    path('maid_list', maid_list, name="maid_list"),
    path('add_biodata', add_biodata, name="add_biodata"),
    path('product', product, name="product"),
    path('agency_cart', agency_cart, name="agency_cart")
]
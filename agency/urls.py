from django.urls import path
from django.conf.urls import url
from .views import add_biodata, agency_cart, enquiry, maid_list, product, edit_biodata, delete_biodata, shortlist_enquiry


urlpatterns = [
    path('', enquiry, name="enquiry"),
    path('shortlist_enquiry', shortlist_enquiry, name="shortlist_enquiry"),
    path('maid_list', maid_list, name="maid_list"),
    path('add_biodata', add_biodata, name="add_biodata"),
    path('product', product, name="product"),
    path('agency_cart', agency_cart, name="agency_cart"),
    path('edit_biodata/<maid_id>', edit_biodata, name="edit_biodata"),
    path('delete_biodata/<maid_id>', delete_biodata, name="delete_biodata")
]
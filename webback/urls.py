from django.urls import path
from django.conf.urls import url
from .views import agency_detail, all_enquiry, all_maid, collection


urlpatterns = [
    path('', agency_detail, name="agency_detail"),
    path('all_enquiry', all_enquiry, name="all_enquiry"),
    path('all_maid', all_maid, name="all_maid"),
    path('collection', collection, name="collection"),
]
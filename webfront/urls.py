# webfront ulrs


from django.urls import path
from django.conf.urls import url
from .views import index, searchmaid, contactus, shortlisted


urlpatterns = [
    path('', index, name="index"),
    path('searchmaid', searchmaid, name="searchmaid"),
    path('shortlisted', shortlisted, name="shortlisted"),
    path('contactus', contactus, name="contactus"),
]
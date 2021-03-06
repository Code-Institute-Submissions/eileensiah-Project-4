# webfront ulrs


from django.urls import path
from django.conf.urls import url
from .views import index, searchmaid, contactus, shortlisted,home, login_required, searchmaidresponsibility


urlpatterns = [
    path('', index, name="index"),
    path('searchmaid', searchmaid, name="searchmaid"),
    path('searchmaidr/<responsibility>', searchmaidresponsibility, name="searchmaidr"),
    path('shortlisted', shortlisted, name="shortlisted"),
    path('contactus', contactus, name="contactus"),
    path('home', home, name="home"),
    path('login_required', login_required, name="login_required"),
]
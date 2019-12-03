from django.urls import path, include
from .views import payment, charge



urlpatterns = [
    path('', payment, name='payment'),
    path('charge', charge, name='charge')
]
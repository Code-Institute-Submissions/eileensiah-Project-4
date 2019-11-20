from django.urls import path
from django.conf.urls import url
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='user_register'),
    path("account_edit/<pk>/", views.account_edit, name="account_edit"),
    url(r'^password/$', views.change_password, name='change_password'),
    # path('logout',  views.logout, name='logout'),
    # path('login',  views.login, name='login'),
    # path('register',  views.register, name='user_register')
]
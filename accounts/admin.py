from django.contrib import admin
from .models import User, Agency, Employer

# paul ecommerce example dont have this
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserLoginForm, UserRegistrationForm




admin.site.register(User)
admin.site.register(Employer)
admin.site.register(Agency)
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import Agency_UserCreationForm, Agency_UserChangeForm
from .models import Agency_User

class Agency_UserAdmin(UserAdmin):
    add_form = Agency_UserCreationForm
    form = Agency_UserChangeForm
    model = Agency_User
    list_display = ['username', 'email', 'agency_name', 'agency_license', 'office_no', 'handphone_no', 'office_address']

admin.site.register(Agency_User, Agency_UserAdmin)


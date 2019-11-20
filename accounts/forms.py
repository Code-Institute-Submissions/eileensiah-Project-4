from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Agency_User

class UserLoginForm(forms.Form):
    """Form is for user login"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class Agency_UserCreationForm(UserCreationForm):

    class Meta:
        model = Agency_User
        fields = ('username', 'email', 'agency_name', 'agency_license', 'office_no', 'handphone_no', 'office_address')

class Agency_UserChangeForm(UserChangeForm):

    class Meta:
        model = Agency_User
        fields = ('username', 'email', 'agency_name', 'agency_license', 'office_no', 'handphone_no', 'office_address')
        
        
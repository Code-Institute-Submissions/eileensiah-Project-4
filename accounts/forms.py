from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db import transaction

# our own user model
from .models import User, Agency, Employer
        


class UserLoginForm(forms.Form):
    """Form is for user login"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
 
    
"""
User registration form
"""
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    def clean_email(self):
        User = get_user_model()
        
        user_provided_email = self.cleaned_data.get('email')
        
        # check if the email already exists inside the User table
        if User.objects.filter(email=user_provided_email):
            # if so, raise an error
            raise forms.ValidationError("This email address is already in use")
        
        return user_provided_email
    
       
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise forms.ValidationError("Please provide your password twice")
        
        if password1 != password2:
            raise forms.ValidationError("Make sure both passwords are the same")
            
        # return password2 as it is becauase it passes all the validtion rules
        return password2
    
        
    class Meta:
        model = User
        fields = ['role','username', 'email', 'password1', 'password2']
       

class AgencySignUpForm(UserCreationForm):
    email = forms.CharField()
    agency_name = forms.CharField()
    agency_license = forms.CharField()
    office_no = forms.CharField()
    handphone_no = forms.CharField()
    office_address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.role = "Agency"
        user.email = self.cleaned_data.get('email')
        user.save()
        agency = Agency.objects.create(user=user)
        agency.agency_name = self.cleaned_data.get('agency_name')
        agency.agency_license = self.cleaned_data.get('agency_license')
        agency.office_no = self.cleaned_data.get('office_no')
        agency.handphone_no = self.cleaned_data.get('handphone_no')
        agency.office_address = self.cleaned_data.get('office_address')
        agency.save()
        return user


class EmployerSignUpForm(UserCreationForm):
    email = forms.CharField()
    name = forms.CharField()
    handphone_no = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.role = "Employer"
        user.email = self.cleaned_data.get('email')
        user.save()
        employer = Employer.objects.create(user=user)
        employer.name = self.cleaned_data.get('name')
        employer.handphone_no = self.cleaned_data.get('handphone_no')
        employer.save()
        return user
  
       
       
       
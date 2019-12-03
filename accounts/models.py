from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass
    role = models.CharField(
        max_length=50,
        choices = [
            ("Employer", "Employer"),
            ("Agency", "Agency")
            ],
        default="Employer"
        )
    
class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    agency_name = models.CharField(max_length=100, blank=False, null=True)
    agency_license = models.CharField(max_length=20, blank=False, null=True)
    office_no = models.CharField(max_length=20, blank=False, null=True)
    office_address = models.CharField(max_length=100, blank=False, null=True)
    handphone_no = models.CharField(max_length=20, blank=False)
    
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=True)
    handphone_no = models.CharField(max_length=20, blank=False)
    

        
        




# accounts/models


from django.contrib.auth.models import AbstractUser
from django.db import models


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
        
    agency_name = models.CharField(max_length=100, blank=False, null=True)
    agency_license = models.CharField(max_length=20, blank=False, null=True)
    office_no = models.CharField(max_length=20, blank=False, null=True)
    office_address = models.CharField(max_length=100, blank=False, null=True)
    handphone_no = models.CharField(max_length=20, blank=False)
    

        
        




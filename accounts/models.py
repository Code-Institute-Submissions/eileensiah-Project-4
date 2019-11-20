from django.contrib.auth.models import AbstractUser
from django.db import models


class Agency_User(AbstractUser):
    pass
    # add additional fields in here
    agency_name = models.CharField(max_length=100)
    agency_license = models.CharField(max_length=20)
    office_no = models.CharField(max_length=20)
    handphone_no = models.CharField(max_length=20)
    office_address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username




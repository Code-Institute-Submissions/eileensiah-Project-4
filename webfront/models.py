from django.db import models


# Create your models here.
class Maid(models.Model):
    name = models.CharField(max_length=30, blank=False)
    nationality = models.CharField(max_length=20, blank=False)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=20, blank=False)
    type_of_maid = models.CharField(max_length=20, blank=False)
    agency_name = models.CharField(max_length=50, blank=False)
    maid_photo = models.ImageField(upload_to="images/maidphoto", default=None)
    
    
    def __str__(self):
        return self.name
        

        
    
    
    
    

from django.db import models
from accounts.models import User


# Create your models here.
class Maid(models.Model):
    name = models.CharField(max_length=30, blank=False)
    
    nationality = models.CharField(
        max_length=50,
        choices = [
            ("Filipino", "Filipino"),
            ("Indonesian", "Indonesian"),
            ("Indian", "Indian"),
            ("Myanmarese", "Myanmarese"),
            ("Others", "Others"),
            ("No Preference", "No Preference"),
            ],
        default="No Preference"
        )
        
    
    type_of_maid = models.CharField(
        max_length=50,
        choices = [
            ("New", "New"),
            ("Transfer", "Transfer"),
            ("Experience", "Experience"),
            ("No Preference", "No Preference"),
            ],
        default="No Preference"    
        )
        
        
    main_responsibility = models.CharField(
        max_length=50,
        choices = [
            ("Cooking", "Cooking"),
            ("Care for Children", "Care for Children"),
            ("Care for Elderly", "Care for Elderly"),
            ("Care for Disabled", "Care for Disabled"),
            ("General Housework", "General Housework"),
            ("No Preference", "No Preference"),
            ],
        default="No Preference"
        )
        
    
    language_ability = models.CharField(
        max_length=50, 
        choices = [
            ("English", "English"),
            ("Mandarin/ Chinese Dialect", "Mandarin/ Chinese Dialect"),
            ("Bahasa Indonesia", "Bahasa Indonesia"),
            ("Hindi/ Tamil", "Hindi/ Tamil"),
            ("Burmese", "Burmese"),
            ("No Preference", "No Preference"),
            ],
        default="No Preference"
        )
        
       
    age = models.CharField(
        max_length=50,
        choices = [
            ("23 to 25", "23 to 25"),
            ("26 to 30", "26 to 30"),
            ("31 to 35", "31 to 35"),
            ("36 to 40", "36 to 40"),
            ("41 to 50", "41 to 50"),
            ("No Preference", "No Preference"),
            ],
        default="No Preference"
        )
        
        
    marital_status = models.CharField(
        max_length=50,
        choices = [
            ("Single", "Single"),
            ("Married", "Married"),
            ("Widowed", "Widowed"),
            ("Divorced", "Divoreced"),
            ("No Preference", "No Preference"),
            ],
        default="No Preference"    
        )
        
        
    agency_name = models.CharField(max_length=50, blank=False)
    agency_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    maid_photo = models.ImageField(upload_to="images/maidphoto", default=None)
    
    
    def __str__(self):
        return self.name
        

        
    
    
    
    

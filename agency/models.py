from django.db import models
from accounts.models import User, Employer,  Agency


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
        
    religion = models.CharField(
        max_length=50,
        choices = [
            ("None", "None"),
            ("Buddhist", "Buddhist"),
            ("Muslim", "Muslim"),
            ("Hindu", "Hindu"),
            ("Christian/ Catholic", "Christian/ Catholic"),
            ("Others", "Others"),
            ],
        default="None"    
        )
    
    no_of_children = models.CharField(
        max_length=50,
        choices = [
            ("None", "None"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("more than 3", "more than 3"),
            ],
        default="None"    
        )
        
    education_level = models.CharField(
        max_length=50,
        choices = [
            ("High School", "High School"),
            ("College", "College"),
            ("Degree", "Degree"),
            ("Others", "Others"),
            ],
        default="Others"    
        )
        
    agency_name = models.CharField(max_length=50, blank=False)
    agency_user = models.ForeignKey(Agency, on_delete=models.CASCADE, default=None)
    maid_photo = models.ImageField(upload_to="images/maidphoto", default=None)
    salary = models.IntegerField(blank=False, default=None)
    date_of_birth = models.DateField(blank=True, default=None)
    employment_history = models.TextField(blank=False, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
        

class Enquiry(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phonenumber = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False)
    enquiry_date = models.DateTimeField(auto_now_add=True)
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
    message = models.TextField(blank=False, default="")
    
    
class Shortlist(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, default=None)
    maid = models.ForeignKey(Maid, on_delete=models.CASCADE, default=None)
    agency = models.CharField(max_length=50, blank=False)
    shortlist_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=False, default="")
    

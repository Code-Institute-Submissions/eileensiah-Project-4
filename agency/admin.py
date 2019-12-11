from django.contrib import admin

from .models import Maid, Shortlist, Enquiry

# Register your models here.

class maidadmin(admin.ModelAdmin):
    list_display = ["name", "nationality", "type_of_maid", "main_responsibility","language_ability", "age", "marital_status"]



class shortlistadmin(admin.ModelAdmin):
    list_display = ["employer", "maid", "agency" , "shortlist_date"]


admin.site.register(Shortlist,shortlistadmin)

admin.site.register(Enquiry)

admin.site.register(Maid,maidadmin)

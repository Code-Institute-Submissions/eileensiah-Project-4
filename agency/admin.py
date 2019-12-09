from django.contrib import admin

from .models import Maid, Shortlist, Enquiry

# Register your models here.
admin.site.register(Maid)

admin.site.register(Shortlist)

admin.site.register(Enquiry)
from django import forms
from .models import Searchmaid


class SearchmaidForm(forms.ModelForm):
    class Meta:
        model = Searchmaid
        fields = ('name', 'nationality', 'age', 'marital_status', 'type_of_maid', 'agency_name', 'maid_photo')
    

    
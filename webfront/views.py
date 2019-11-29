from django.shortcuts import render, HttpResponse
from webfront.models import Maid

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, "index.html")
    
  
def searchmaid(request):
    searchmaid = Maid.objects.all()
    return render(request, "searchmaid.html")
    

# add search maid form   
# def add_searchmaid(request):
#     if request.method == "POST":
#         form = SearchmaidForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("searchmaid")
#     else:
#         form = SearchmaidForm()
#     return render(request, 'searchmaid_form.html',{
#              "form":form
#         })


# edit search maid data
# def edit_searchmaid(request, searchmaid_id):
#     searchmaid = get_object_or_404(Searchmaid,id=searchmaid_id)
    
#     if request.method == "POST":
#         form = SearchmaidForm(request.POST or None, request.FILES or None, instance=searchmaid)
#         if form.is_valid():
#             form.save()
#         return redirect("searchmaid")
#     else:
#         form = SearchmaidForm(instance=searchmaid)
#         return render(request, 'edit_searchmaid_form.html',{
#              "form":form
#         })
    

def contactus(request):
    return render(request, "contactus.html")  
    
    
    
def shortlisted(request):
    return render(request, "shortlisted.html")  
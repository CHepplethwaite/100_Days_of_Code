from django.shortcuts import render
from django.views.generic import CreateView,DeleteView
from .models import PatientInfo


#def index(request):
 #   return render(request,"crud_app/index.html",{})

class CreateCBV(CreateView):
    model=PatientInfo
    fields=["first_name",
    "last_name", 
    "age",
    "phone_number",
    "address",
    "comment",
    "image",
    "national_id"
    ]


from django.shortcuts import render
from django.views.generic import CreateView,DeleteView
from django.urls import reverse_lazy
from .models import PatientInfo
from django.views.generic.edit import UpdateView


#def index(request):
 #   return render(request,"crud_app/index.html",{})

class CreateCBV(CreateView): # uses modelname_form.html form
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
    success_url=reverse_lazy('list')


class DeleteCBV(DeleteView):
    model=PatientInfo
    success_url=reverse_lazy('list')


class UpdateCBV(UpdateView):
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
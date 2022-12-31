from django import forms
from .models import PatientInfo

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientInfo
        fields = "__all__"

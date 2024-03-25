from django import forms

from .models import DoctorBook
from django.forms.models import inlineformset_factory

class DoctorBookForm(forms.ModelForm):
    class Meta:
        model = DoctorBook
        fields = ['doctor','civil_id','date_from', 'date_to']
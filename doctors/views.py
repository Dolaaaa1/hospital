from django.shortcuts import render ,redirect
from .models import Doctor
from django_filters.views import FilterView

from django.views.generic.edit import FormMixin
from django.views.generic import ListView ,DetailView ,CreateView
from .forms import DoctorBookForm
from django.db.models.query_utils import Q

# Create your views here.

class DoctorList(ListView):
    model = Doctor
    paginate_by = 1
  
    template_name ='doctors/doctor_list.html'
    
    
    
    
class DoctorDetail(FormMixin,DetailView):
    model = Doctor
    form_class = DoctorBookForm
    template_name ='doctors/doctor_detail.html'
    
    def get_queryset(self):
        name = self.request.GET.get('q','')
        object_list = Doctor.objects.filter(
            Q(name__icontains=name) |
            Q(specialty__icontains=name)
         )
        return object_list 
    
    

    
    def post(self,request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()
            
            return redirect('/')    

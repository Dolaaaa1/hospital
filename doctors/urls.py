from django.urls import path
from .views import DoctorList ,DoctorDetail



app_name = 'doctor'

urlpatterns = [
    path('',DoctorList.as_view(),name='doctors_list'),
    path('<slug:slug>',DoctorDetail.as_view(),name='doctors_detail'),

]
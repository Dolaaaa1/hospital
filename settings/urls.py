from django.urls import path
from .views import *


app_name = 'settings'

urlpatterns = [
    path('',home , name='home'),

]
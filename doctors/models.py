from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor/')
    specialty =models.TextField(max_length=10000)
    phone_number = models.CharField(max_length=20)
    slug = models.SlugField(null= True,blank=True) 
    
    def __str__(self):
        return self.name
      
    def get_absolute_url(self):
        return reverse('doctors:doctors_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
       if not self.slug:
         self.slug = slugify(self.name)
       super(Doctor, self).save(*args, **kwargs)
       
 
    
    
#    class Patient(models.Model):
#        age = models.IntegerField(default=0)
#        gender = models.CharField(max_length=20)
#        phone_number1 = models.CharField(max_length=20)
#        phone_number2 = models.CharField(max_length=20)
#        email = models.EmailField()
        
#        def __str__(self):
#            return self.name
    
#    class Appointment(models.Model):
#        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#        date_time = models.DateTimeField()
    
class DoctorBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    civil_id =models.CharField(max_length=16)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    
    
    
    def __str__(self):
        return self.user

    
    

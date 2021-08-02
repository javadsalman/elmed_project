from doctor.models import Doctor
from departament.models import Departament
from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Ad Soyad")
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Müraciət Edilən Şöbə")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Müraciət Edilən Həkim")
    email = models.EmailField(max_length=50, verbose_name="Email Ünvanı", null=True, blank=True)
    phone = models.CharField(max_length=50, null=False, verbose_name="Telefon Nömrəsi")
    date = models.DateField(verbose_name="Müraciət Tarixi", null=True, blank=True)
    time = models.TimeField(verbose_name="Müraciət Saatı", null=True, blank=True)
    note = models.TextField(verbose_name="Qeyd")
    seen = models.BooleanField(default=False, verbose_name="Baxıldı")
    updated = models.DateTimeField(auto_now=True, verbose_name="Son Dəyişdirilmə Tarixi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma Tarixi")
    
    class Meta:
        ordering = ['-updated']
        verbose_name = 'Randevu'
        verbose_name_plural = 'Randevular'

    def __str__(self):
        return self.name
from django.db import models
import datetime

from django.db.models.fields import CharField

nine_oclock = datetime.time(9, 0)
seventeen_oclock = datetime.time(17, 0)

class Schedule(models.Model):
    title = models.CharField(max_length=100, verbose_name="Iş Rejmi Adı")
    show_schedule = models.BooleanField(default=True, verbose_name="İş rejmini Saytda Göstərilsin")
    monday_show = models.BooleanField(default=True, verbose_name="Bazar Ertəsi Rejmi Göstərilsin")
    monday_start = models.TimeField(default=nine_oclock, verbose_name="Bazar Ertəsi Başlanğıc")
    monday_end = models.TimeField(default=seventeen_oclock, verbose_name="Bazar Ertəsi Bitmə")
    tuesday_show = models.BooleanField(default=True, verbose_name="Çərşənbə Axşamı Rejmi Göstərilsin")
    tuesday_start = models.TimeField(default=nine_oclock, verbose_name="Çərşənbə Axşamı Başlanğıc")
    tuesday_end = models.TimeField(default=seventeen_oclock, verbose_name="Çəşənbə Axşamı Bitiş")
    wednesday_show = models.BooleanField(default=True, verbose_name="Çəşənbə Rejmi Göstərilsin")
    wednesday_start = models.TimeField(default=nine_oclock, verbose_name="Çəşənbə Başlanğıc")
    wednesday_end = models.TimeField(default=seventeen_oclock, verbose_name="Çəşənbə Bitiş")
    thursday_show = models.BooleanField(default=True, verbose_name="Cümə Axşamı Rejmi Göstərilsin")
    thursday_start = models.TimeField(default=nine_oclock, verbose_name="Cümə Axşamı Başlanğıc")
    thursday_end = models.TimeField(default=seventeen_oclock, verbose_name="Cümə Axşamı Bitiş")
    friday_show = models.BooleanField(default=True, verbose_name="Cümə Rejmi Göstərilsin")
    friday_start = models.TimeField(default=nine_oclock, verbose_name="Cümə Başlanğıc")
    friday_end = models.TimeField(default=seventeen_oclock, verbose_name="Cümə Bitiş")
    saturday_show = models.BooleanField(default=True, verbose_name="Şənbə Rejmi Göstərilsin")
    saturday_start = models.TimeField(default=nine_oclock, verbose_name="Şənbə Başlanğıc")
    saturday_end = models.TimeField(default=seventeen_oclock, verbose_name="Şənbə Bitiş")
    sunday_show = models.BooleanField(default=False, verbose_name="Bazar Rejmi Göstərilsin")
    sunday_start = models.TimeField(default=nine_oclock, verbose_name="Bazar Başlanğıc")
    sunday_end = models.TimeField(default=seventeen_oclock, verbose_name="Bazar Bitiş")
    updated = models.DateTimeField(auto_now=True, verbose_name="Son Dəyişdirilmə Tarixi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma Tarixi")
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.title
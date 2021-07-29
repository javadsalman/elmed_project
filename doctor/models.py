from ckeditor.fields import RichTextField
from shared.model.utils import get_image_tag, get_slug, get_slug_link
from shared.model.abstracts import Schedule
from departament.models import Departament
from django.db import models
from imagekit.models import ProcessedImageField
from departament.models import Departament
from django.urls import reverse
from django.contrib.auth.models import User

class DoctorSchedule(Schedule):
    class Meta:
        verbose_name = "Həkim İş Rejmi"
        verbose_name_plural = "Həkim İş Rejimləri"

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='İstifadəçi Hesabı')
    name = models.CharField(max_length=50, verbose_name='Ad Soyad')
    slug = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='doctor/image/', options={'quality': 90}, verbose_name='Şəkil')
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True, verbose_name='Şöbə')
    about = RichTextField(null=False, blank=True, verbose_name='Haqqında Məlumat')
    profession = models.CharField(max_length=100, verbose_name='Vəzifəsi')
    degree = models.CharField(max_length=150, verbose_name='Dərəcəsi')
    facebook = models.URLField(max_length=300, verbose_name='Facebook Linki')
    instagram = models.URLField(max_length=300, verbose_name='Instagram Linki')
    whatsapp = models.URLField(max_length=300, verbose_name='Whatsapp Linki')
    youtube = models.URLField(max_length=300, verbose_name='YouTube Linki')
    phone = models.CharField(max_length=50, verbose_name='Telefon Nömrəsi')
    schedule = models.ForeignKey(DoctorSchedule, on_delete=models.PROTECT, verbose_name='İş Rejmi')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Son Dəyişdirilmə Tarixi')
    created = models.DateTimeField(auto_now=True, verbose_name='Yaradılma Tarixi')
    
    class Meta:
        ordering = ['name']
        verbose_name = "Həkim"
        verbose_name_plural = "Həkimlər"
    
    def save(self, *args, **kwargs):
        self.slug = get_slug(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return '%s - %s' % (self.name, self.profession)
        
    def get_absolute_url(self):
        return reverse("doctor-detail", args=[self.id, self.slug])
    
    def image_tag(self):
        return get_image_tag(self.image.url)
    image_tag.short_description = 'Mövcud Həkim Şəkli'
    
    def slug_link(self):
        return get_slug_link(self.slug, self.get_absolute_url)

    slug_link.short_description = 'Link'
    
    
    

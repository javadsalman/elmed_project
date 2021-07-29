from shared.model.utils import get_image_tag, get_slug, get_slug_link
from shared.model.abstracts import Schedule
from django.db import models
from imagekit.models import ProcessedImageField
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.

class DepartamentSchedule(Schedule):
    class Meta:
        verbose_name = "Şöbə İş Rejmi"
        verbose_name_plural = "Şöbə İş Rejimləri"

class Departament(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name="Şöbə adı")
    description = models.TextField(null=False, blank=False, verbose_name="Qısa Məlumat")
    icon = ProcessedImageField(upload_to='departament/icons/', options={'quality': 70}, null=False, verbose_name="İkon")
    slug = models.SlugField(max_length=100, unique=True, default='', blank=True)
    about = RichTextField(null=False, blank=True, verbose_name="Haqqında Məlumat")
    schedule = models.ForeignKey(DepartamentSchedule, on_delete=models.PROTECT, verbose_name="İş Rejmi")
    updated = models.DateTimeField(auto_now=True, verbose_name="Son Dəyişdirilmə Tarixi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma Tarixi")
    
    class Meta:
        ordering = ['name']
        verbose_name = "Şöbə"
        verbose_name_plural = "Şöbələr"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("departament_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = get_slug(self.name)
        super().save(*args, **kwargs)
        
    def icon_tag(self):
        return get_image_tag(self.icon.url)
    icon_tag.short_description = 'Mövcud İkon'
    
    def slug_link(self):
        return get_slug_link(self.slug, self.get_absolute_url)
    slug_link.short_description = 'Link'

        

class DepartamentImage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlıq")
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='departament/images/', options={'quality': 90}, verbose_name="Şəkil Faylı")
    def image_tag(self):
        return get_image_tag(self.image.url)
    image_tag.short_description = 'Mövcud Şəkil'
    updated = models.DateTimeField(auto_now=True, verbose_name="Son Dəyişdirilmə Tarixi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma Tarixi")
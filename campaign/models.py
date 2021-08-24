from shared.model.utils import get_image_tag, get_slug, get_slug_link
from django.db import models
from departament.models import Departament
from imagekit.models import ProcessedImageField, ImageSpecField
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Campaign(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True, verbose_name='Şöbə')
    slug = models.SlugField(max_length=100)
    price = models.FloatField(verbose_name='Qiymət AZN')
    date_interval = models.CharField(max_length=50, null=True, blank=True, verbose_name='Aktiv Tarixlər')
    time_interval = models.CharField(max_length=50, null=True, blank=True, verbose_name='Aktiv Saatlar')
    available = models.BooleanField(default=True, verbose_name='Davam Edir')
    first_image = ProcessedImageField(upload_to='campaign/first/', options={'quality': 180}, verbose_name='Əsas Şəkil')
    second_image = ProcessedImageField(upload_to='campaign/second/', options={'quality': 180}, null=True, blank=True, verbose_name='İkinci Şəkil')
    third_image = ProcessedImageField(upload_to='campaign/third/', options={'quality': 180}, null=True, blank=True, verbose_name='Üçüncü Şəkil')
    thumbnail = ImageSpecField(source=first_image, format='JPEG', options={'quality': 80})
    show = models.BooleanField(default=True, verbose_name='Saytda Görünsün')
    about = RichTextField(verbose_name='Ətraflı')
    updated = models.DateTimeField(auto_now=True, verbose_name='Son Dəyişdirilmə Tarixi')
    created = models.DateTimeField(auto_now=True, verbose_name='Yaradılma Tarixi')
    
    def save(self, *args, **kwargs):
        self.slug = get_slug(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("campaign-detail", kwargs={"pk": self.pk, "slug": self.slug})
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated']
        verbose_name = 'Kampaniya'
        verbose_name_plural = 'Kampaniyalar'
        
    def slug_link(self):
        return get_slug_link(self.slug, self.get_absolute_url)
    slug_link.short_description = 'Link'
        
    def first_image_tag(self):
        return get_image_tag(self.first_image.url)
    first_image_tag.short_description = 'Mövcud Əsas Şəkil'
    
    def second_image_tag(self):
        return get_image_tag(self.second_image.url)
    second_image_tag.short_description = 'Mövcud İkinci Şəkil'
    
    def third_image_tag(self):
        return get_image_tag(self.third_image.url)
    third_image_tag.short_description = 'Mövcud Üçüncü Şəkil'



"""
title
departament
price
start (datetime)
stop (datetime)
does continue
first image
second image
third image
show
about
updated
created
"""
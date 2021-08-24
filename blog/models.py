from ckeditor.fields import RichTextField
from doctor.models import Doctor
from shared.model.utils import get_image_tag, get_slug, get_slug_link, text_from_html
from django.db import models
from django.urls.base import reverse
from imagekit.models import ProcessedImageField, ImageSpecField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name="Ad")
    slug = models.SlugField(max_length=100)
    cover = ProcessedImageField(upload_to='blog/category/cover/', options={'quality': 180}, verbose_name="Qapaq Şəkli", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Son Dəyişdirilmə Tarixi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma Tarixi")
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def get_absolute_url(self):
        return reverse('blog') + '?category=%s' % self.slug
    
    def slug_link(self):
        return get_slug_link(self.slug, self.get_absolute_url)
    slug_link.short_description = 'Link'
    
    def cover_tag(self):
        return get_image_tag(self.cover.url)
    cover_tag.short_description = 'Mövcud Qapaq Şəkli'
    
    def save(self, *args, **kwargs):
        self.slug = get_slug(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
        
        
class Article(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, default=None, verbose_name="Müəllif")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Kateqoriya")
    title = models.CharField(max_length=60, null=False, blank=False, verbose_name="Başlıq")
    description = models.CharField(max_length=200, null=True, blank=True)
    main_image = ProcessedImageField(upload_to='article/main_images/', verbose_name="Əsas Şəkil", options={'quality': 180})
    thumbnail = ImageSpecField(source='main_image', format='JPEG', options={'quality': 80})
    slug = models.SlugField(max_length=100)
    content = RichTextField(verbose_name="Kontent")
    show = models.BooleanField(default=True, verbose_name='Bloqda görünsünmü?')
    updated = models.DateTimeField(auto_now=True, verbose_name="Son Dəyişdirilmə Tarixi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma Tarixi")
    
    
    class Meta:
        ordering = ['-updated']
        verbose_name = 'Məqalə'
        verbose_name_plural = 'Məqalələr'
    
    def save(self, *args, **kwargs):
        self.slug = get_slug(self.title)
        self.description = text_from_html(self.content)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return '%s - %s' % (self.title, self.doctor.name if self.doctor else 'Ümumi')
        
    def get_absolute_url(self):
        return reverse("article", kwargs={"pk": self.pk, "slug": self.slug})
        
    def related_articles(self):
        return self.category.article_set.exclude(pk=self.pk)[:4]
    
    def slug_link(self):
        return get_slug_link(self.slug, self.get_absolute_url)
    slug_link.short_description = 'Link'
    
    def main_image_tag(self):
        return get_image_tag(self.main_image.url)
    main_image_tag.short_description = 'Mövcud Əsas Şəkil'
    

        
class ArticleImage(models.Model):
    image = ProcessedImageField(upload_to='blog/article/images/', options={'quality': 90}, verbose_name="Şəkil Faylı")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma Tarixi")
    
    class Meta:
        verbose_name = 'Məqalə Şəkli'
        verbose_name_plural = 'Məqalə Şəkilləri'

    def image_tag(self):
        return get_image_tag(self.image.url)
    image_tag.short_description = 'Mövcud Şəkil'
    
    
    
    
from django.contrib import admin
from django.utils.html import format_html
from blog.models import Category, Article, ArticleImage

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'cover_tag', 'cover', 'slug_link']
    readonly_fields = ['cover_tag', 'slug_link']
    list_display = ['name', 'category_link', 'created']

    def category_link(self, obj):
        return format_html('<a href="{}"><b>GET</b></a>', obj.get_absolute_url())
    category_link.short_description = 'Keçid Linki'





class ArticleImageInline(admin.TabularInline):
    fields = ['title', 'image_tag', 'image', 'created']
    readonly_fields = ['image_tag', 'created']
    model = ArticleImage
    extra = 1


@admin.action(description='Seçilənlər Bloqda Görünsün')
def show_article_action(modeladmin, request, queryset):
    queryset.update(show=True)

@admin.action(description='Seçilənlər Bloqda Görünməsin')
def hide_article_action(modeladmin, request, queryset):
    queryset.update(show=False)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'doctor',
        'title',
        'main_image_tag', 
        'main_image', 
        'category', 
        'content',
        'show',
        'slug_link', 
        'updated', 
        'created']
    
    readonly_fields = ['slug_link', 'main_image_tag', 'updated', 'created']
    
    inlines = [ArticleImageInline]
    actions = [show_article_action, hide_article_action]
    
    list_display = ['title', 'doctor_link', 'category_link', 'article_link', 'show', 'updated']
    
    def article_link(self, obj):
        return format_html('<a href="{}" target="_blank"><b>GET</b></a>', obj.get_absolute_url())
    article_link.short_description = 'Keçid Linki'
    
    def doctor_link(self, obj):
        if obj.doctor:
            return format_html(
                '<a href="{}">{}</a>', 
                obj.doctor.get_absolute_url(), 
                f'Dr. {obj.doctor.name.split()[0]}'
            )
        else:
            return 'Ümumi'
    doctor_link.short_description = 'Müəllif'
    
    def category_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.category.get_absolute_url(), obj.category.name)
    category_link.short_description = 'Kateqoriya'
    
    
from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.utils.html import format_html
from doctor.models import Doctor, DoctorSchedule

# Register your models here.
admin.site.register(DoctorSchedule)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    fields = [
        'user',
        'name',
        'image_tag',
        'image',
        'departament',
        'schedule',
        'profession',
        'degree',
        'about',
        'facebook',
        'instagram',
        'whatsapp',
        'youtube',
        'phone',
        'slug_link',
        'updated',
        'created'
        ]
    
    readonly_fields = ['slug_link', 'image_tag', 'updated', 'created']
    
    list_display = ['name', 'profession', 'departament_link', 'updated']
    list_filter = ['departament']
    
    def departament_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.departament.get_absolute_url(), obj.departament.name)
    departament_link.short_description = 'Şöbə'
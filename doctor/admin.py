from django.contrib import admin
from django.contrib.admin.options import TabularInline
from django.utils.html import format_html
from doctor.models import Doctor, DoctorSchedule, DoctorEducation

# Register your models here.
@admin.action(description='Seçilənləri Saytda Gizlət')
def hide_schedule_action(modeladmin, request, queryset):
    queryset.update(show_schedule=False)

@admin.action(description='Seçilənləri Saytda Göstər')
def show_schedule_action(modeladmin, request, queryset):
    queryset.update(show_schedule=True)

@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_schedule', 'updated']
    list_filter = ['show_schedule']
    actions = [hide_schedule_action, show_schedule_action]
    

class DoctorEducationInline(TabularInline):
    model = DoctorEducation
    extra = 1

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
        'phone',
        'email',
        'facebook',
        'instagram',
        'whatsapp',
        'youtube',
        'slug_link',
        'updated',
        'created'
        ]
    
    readonly_fields = ['slug_link', 'image_tag', 'updated', 'created']
    
    list_display = ['name', 'profession', 'departament_link', 'updated']
    list_filter = ['departament']
    inlines = [DoctorEducationInline]
    
    def departament_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.departament.get_absolute_url(), obj.departament.name)
    departament_link.short_description = 'Şöbə'
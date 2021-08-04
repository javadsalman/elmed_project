from appointment.models import Appointment
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

@admin.action(description='Seçilənləri Baxıldı Et')
def make_seen(modeladmin, request, queryset):
    queryset.update(seen=True)

@admin.action(description='Seçilənləri Baxılmadı Et')
def make_unseen(modeladmin, request, queryset):
    queryset.update(seen=False)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ['seen']
    list_display = ['name', 'departament_link', 'doctor_link', 'phone', 'seen']
    list_filter = ['seen', 'departament', 'created']
    
    actions = [make_seen, make_unseen]
    
    def doctor_link(self, obj):
        if obj.doctor:
            return format_html(
                '<a href="{}" target="_blank">{}</a>', 
                obj.doctor.get_absolute_url(), 
                f'Dr. {obj.doctor.name.split()[0]}')
        else:
            return None
    doctor_link.short_description = 'Həkim'
        
    def departament_link(self, obj):
        if obj.departament:
            return format_html(
                '<a href="{}">{}</a>', 
                obj.departament.get_absolute_url(), 
                obj.departament.name)
        else:
            return None
    departament_link.short_description = 'Şöbə'
    
from django.contrib import admin
from django.utils.html import format_html
from departament.models import Departament, DepartamentImage, DepartamentSchedule

# Register your models here.
@admin.action(description='Seçilənləri Saytda Gizlət')
def hide_schedule_action(modeladmin, request, queryset):
    queryset.update(show_schedule=False)

@admin.action(description='Seçilənləri Saytda Göstər')
def show_schedule_action(modeladmin, request, queryset):
    queryset.update(show_schedule=True)

@admin.register(DepartamentSchedule)
class DepartamentScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_schedule', 'updated']
    actions = [hide_schedule_action, show_schedule_action]


class DepartamentImageInline(admin.TabularInline):
    fields = ['image_tag', 'image', 'created']
    readonly_fields = ['image_tag', 'created']
    model = DepartamentImage
    extra = 1

@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'icon_tag', 'icon', 'schedule', 'about', 'slug_link', 'updated', 'created']
    readonly_fields = ['slug_link', 'icon_tag', 'updated', 'created']
    inlines = [DepartamentImageInline]
    
    list_display = ['name', 'departament_link', 'updated']
    def departament_link(self, obj):
        return format_html('<a href="{}" target="_blank"><b>GET</b></a>', obj.get_absolute_url())
    departament_link.short_description = 'Keçid Linki'
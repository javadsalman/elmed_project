from django.contrib import admin
from django.utils.html import format_html
from campaign.models import Campaign

# Register your models here.

@admin.action(description='Seçilənlər Saytda Görünməsin')
def show_campaign_action(modeladmin, request, queryset):
    queryset.update(show=True)
    
@admin.action(description='Seçilənlər Saytda Görünməsin')
def hide_campaign_action(modeladmin, request, queryset):
    queryset.update(show=False)
    
    
@admin.action(description='Seçilənlər Davam Etsin')
def active_campaign_action(modeladmin, request, queryset):
    queryset.update(available=True)
    
@admin.action(description='Seçilənlər Davam Etməsin')
def deactive_campaign_action(modeladmin, request, queryset):
    queryset.update(available=False)
    
    

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'departament',
        'price',
        'date_interval',
        'time_interval',
        'available',
        'first_image_tag',
        'first_image',
        'second_image_tag',
        'second_image',
        'third_image_tag',
        'third_image',
        'show',
        'about',
        'slug_link',
        'updated',
        'created',
    ]
    
    readonly_fields = [
        'first_image_tag',
        'second_image_tag',
        'third_image_tag',
        'slug_link',
        'updated',
        'created',
    ]
    
    list_display = ['title', 'departament', 'price', 'date_interval', 'available', 'show', 'campaign_link', 'updated_date']
    list_filter = ['departament', 'updated']
    
    actions = [show_campaign_action, hide_campaign_action, active_campaign_action, deactive_campaign_action]

    def updated_date(self, obj):
        return obj.updated.strftime('%d.%m.%Y')
    updated_date.short_description = 'Dəyişdirildi'
    
    def campaign_link(self, obj):
        return format_html('<a href="{}" target="_blank"><b>GET</b></a>', obj.get_absolute_url())
    campaign_link.short_description = 'Keçid Linki'
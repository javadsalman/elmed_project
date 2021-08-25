from campaign.models import Campaign
import django_filters

class CampaignFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    departament = django_filters.CharFilter(field_name='departament', lookup_expr='slug')
    
    class Meta:
        model = Campaign
        fields = ['title', 'departament']
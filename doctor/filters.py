import django_filters
from doctor.models import Doctor

class DoctorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    departament = django_filters.CharFilter(field_name='departament', lookup_expr='id')
    
    class Meta:
        model = Doctor
        fields = ['name', 'departament']
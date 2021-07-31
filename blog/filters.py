from blog.models import Article
import django_filters

class BlogFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category', lookup_expr='slug')
    
    class Meta:
        model = Article
        fields = ['title', 'category']
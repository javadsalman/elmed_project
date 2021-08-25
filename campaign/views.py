from django.views.generic import DetailView
from shared.pagination.pagination import get_page_list
from campaign.filters import CampaignFilter
from campaign.models import Campaign
from django.shortcuts import render
from django_filters.views import FilterView
from django.db.models import Count
from departament.models import Departament

# Create your views here.
class CapmapignList(FilterView):
    template_name = 'campaign/campaign_list/campaign_list.html'
    filterset_class = CampaignFilter
    paginate_by = 6
    
    def get_queryset(self):
        return Campaign.objects.filter(show=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_list'] = get_page_list(context['page_obj'].number, context['page_obj'].paginator.num_pages, self.paginate_by)
        context['departaments'] = Departament.objects.all().annotate(campaign_nums=Count('campaign'))
        context['total_count'] = self.get_queryset().count()
        return context


class CapmapignDetail(DetailView):
    model = Campaign
    template_name = 'campaign/campaign_detail/campaign_detail.html'
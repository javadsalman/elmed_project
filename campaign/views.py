from django.shortcuts import render
from django_filters.views import FilterView

# Create your views here.
def CapmapignList(request):
    return render(request, 'campaign/campaign_list/campaign_list.html')

# class CapmapignList(FilterView):
#     template_name = 'campaign/campaign_list/campaign_list.html'
#     context_object_name = 'campaigns'
#     model = 

def CapmapignDetail(request, pk, slug):
    return render(request, 'campaign/campaign_detail/campaign_detail.html')
from django.urls import path
from campaign.views import CapmapignList, CapmapignDetail

urlpatterns = [
    path('', CapmapignList.as_view(), name='campaign-list'),
    path('<int:pk>/<str:slug>/', CapmapignDetail.as_view(), name='campaign-detail')
]

from django.urls import path
from campaign.views import CapmapignList, CapmapignDetail

urlpatterns = [
    path('', CapmapignList, name='campaign-list'),
    path('<int:pk>/<str:slug>/', CapmapignDetail, name='campaign-detail')
]

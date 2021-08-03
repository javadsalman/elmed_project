from django.urls import path
from departament.views import DepartamentList, DepartamentDetail

urlpatterns = [
    path('', DepartamentList.as_view(), name='departament-list'),
    path('<slug:slug>/', DepartamentDetail.as_view(), name='departament_detail'),
]

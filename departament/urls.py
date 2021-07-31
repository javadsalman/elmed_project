from django.urls import path
from departament.views import DepartamentList, depertament_detail

urlpatterns = [
    path('', DepartamentList.as_view(), name='departament-list'),
    path('<slug:slug>/', depertament_detail, name='departament_detail'),
]

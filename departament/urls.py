from django.urls import path
from departament.views import departaments, depertament_detail

urlpatterns = [
    path('', departaments, name='departament-list'),
    path('detail/', depertament_detail, name='departament_detail'),
]

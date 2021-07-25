from django.urls import path
from departament.views import departaments

urlpatterns = [
    path('', departaments, name='departament-list'),
]

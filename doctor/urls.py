from django.urls import path
from doctor.views import doctors

urlpatterns = [
    path('', doctors, name='doctor-list'),
]

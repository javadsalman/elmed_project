from django.urls import path
from doctor.views import doctors, doctor_detail

urlpatterns = [
    path('', doctors, name='doctor-list'),
    path('detail', doctor_detail, name='doctor-detail')
]

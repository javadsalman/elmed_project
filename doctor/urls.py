from django.urls import path
from doctor.views import DoctorList, doctor_detail

urlpatterns = [
    path('', DoctorList.as_view(), name='doctor-list'),
    path('<int:pk>/<str:slug>/', doctor_detail, name='doctor-detail')
]

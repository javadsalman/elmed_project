from django.urls import path
from doctor.views import DoctorList, DoctorDetail

urlpatterns = [
    path('', DoctorList.as_view(), name='doctor-list'),
    path('<int:pk>/<str:slug>/', DoctorDetail.as_view(), name='doctor-detail')
]

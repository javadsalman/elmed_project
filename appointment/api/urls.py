from appointment.api.views import AppointmentList, AppointmentDetail, logout_view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('appointment-list/', AppointmentList.as_view(), name='appointment-list'),
    path('appointment-list/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout')
]
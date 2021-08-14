from appointment.api.views import AppointmentList, AppointmentDetail, edit_list, logout_view, login_view, search
from django.urls import path

urlpatterns = [
    path('appointment-list/', AppointmentList.as_view(), name='appointment-list'),
    path('appointment-list/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
    path('appointment-list/edit/', edit_list, name='appointment-detail'),
    path('login/', login_view, name='reception-login'),
    path('logout/', logout_view, name='reception-logout'),
    path('search/', search, name='appointment-search')
]
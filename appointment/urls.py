from django.urls import path
from appointment.views import appointment, feedback

urlpatterns = [
    path('', appointment, name='appointment'),
    path('melumat/<str:result>', feedback, name='feedback'),
]

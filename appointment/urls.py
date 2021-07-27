from django.urls import path
from appointment.views import appointment

urlpatterns = [
    path('', appointment, name='appointment'),
]

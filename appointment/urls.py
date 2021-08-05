from django.urls.conf import include
from django.urls import path
from appointment.views import appointment, feedback
from os import getenv

urlpatterns = [
    path('', appointment, name='appointment'),
    path('melumat/<str:result>', feedback, name='feedback'),
]

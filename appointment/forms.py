from django.forms import ModelForm
from appointment.models import Appointment

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ['updated', 'created', 'seen']
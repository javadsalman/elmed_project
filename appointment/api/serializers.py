from rest_framework import serializers
from appointment.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    doctor_name = serializers.SerializerMethodField()
    departament_name = serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        exclude = ['updated']
        
    
    def get_created(self, obj):
        return obj.created.strftime('%H:%M %d.%m.%Y')
    
    def get_doctor_name(self, obj):
        if obj.doctor:
            return obj.doctor.name
        else:
            return None
        
    def get_departament_name(self, obj):
        if obj.departament:
            return obj.departament.name
        else:
            return None
    
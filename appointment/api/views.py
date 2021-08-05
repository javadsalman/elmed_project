from rest_framework.response import Response
from appointment.api.serializers import AppointmentSerializer
from appointment.models import Appointment
from rest_framework import generics, decorators, status
from django.contrib.auth import logout


class AppointmentList(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    

class AppointmentDetail(generics.RetrieveDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.seen = True
        obj.save()
        return super().retrieve(request, *args, **kwargs)
    
@decorators.api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()
    logout(request)
    return Response(status=status.HTTP_200_OK)
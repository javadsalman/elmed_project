from departament.models import Departament
from doctor.models import Doctor
from appointment.api.permissions import IsReceptionStaff
from rest_framework.response import Response
from appointment.api.serializers import AppointmentSerializer
from appointment.models import Appointment
from rest_framework import generics, decorators, status
from django.contrib.auth import logout, authenticate
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class AppointmentList(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsReceptionStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seen', 'name', 'doctor', 'departament']
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        seen_count = self.queryset.filter(seen=True).count()
        unseen_count = self.queryset.filter(seen=False).count()
        response.data['seenCount'] = seen_count
        response.data['unseenCount'] = unseen_count
        return response
        
    

class AppointmentDetail(generics.RetrieveDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes=[IsReceptionStaff]
    
    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.seen:
            obj.seen = True
            obj.save()
        return super().retrieve(request, *args, **kwargs)
    
@decorators.api_view(['POST'])
@decorators.permission_classes([IsReceptionStaff])
def logout_view(request):
    request.user.auth_token.delete()
    logout(request)
    return Response(status=status.HTTP_200_OK)


@decorators.api_view(['POST'])
@decorators.throttle_classes([UserRateThrottle, AnonRateThrottle])
def login_view(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user != None and 'appointment.view_appointment' in user.get_all_permissions():
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@decorators.api_view(['GET'])
@decorators.permission_classes([IsReceptionStaff])
def search(request):
    search_type = request.query_params['searchType']
    search_value = request.query_params['searchValue']
    if search_type == 'name':
        queryset = Appointment.objects.filter(name__icontains=search_value)
    elif search_type == 'doctor':
        queryset = Doctor.objects.filter(name__icontains=search_value)
    elif search_type == 'departament':
        queryset = Departament.objects.filter(name__icontains=search_value)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(queryset[:6].values('id', 'name'))


@decorators.api_view(['PUT'])
@decorators.permission_classes([IsReceptionStaff])
def edit_list(request):
    edit_type = request.data['editType']
    id_list = request.data['idList']
    if isinstance(id_list, list):
        appointments = Appointment.objects.filter(id__in=id_list)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if edit_type == 'seen':
        appointments.update(seen=True)
    elif edit_type == 'unseen':
        appointments.update(seen=False)
    elif edit_type == 'delete':
        appointments.delete()
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)

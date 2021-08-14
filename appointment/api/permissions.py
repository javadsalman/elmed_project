from rest_framework import permissions

class IsReceptionStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return 'appointment.view_appointment' in request.user.get_all_permissions()
            
from rest_framework import permissions

class IsReceptionStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.has_perm('appointment.view_appointment')
            
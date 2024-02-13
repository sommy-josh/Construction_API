from rest_framework.permissions import BasePermission

class CanViewProductOnly(BasePermission):
    def has_object_permission(self, request, view):
        if request.method=='GET':
            return True
        
        return False
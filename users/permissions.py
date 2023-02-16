from rest_framework import permissions
from users.models import User
from rest_framework.views import Request, View
import ipdb


class SuperAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (
            request.user.is_authenticated and request.user.is_superuser
        )


class IsProfileOwner(permissions.BasePermission):
    
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:

        if request.user.is_superuser and request.user.is_authenticated:
            return True
        
        return request.user.is_authenticated and request.user.id == user.id
        

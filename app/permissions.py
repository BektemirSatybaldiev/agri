from rest_framework import permissions


class IsFarmer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.farmer.user == request.user

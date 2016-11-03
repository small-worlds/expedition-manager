from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsRegistrantOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.method == 'POST':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsRegistrant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

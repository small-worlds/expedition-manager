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
        elif request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsRegistrant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsStaffOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow user to list all users if logged in user is staff
        if request.method == 'POST' and not request.user.is_authenticated:
            return True
        elif not request.user.is_authenticated and request.method != 'POST':
            return False
        elif request.method in permissions.SAFE_METHODS:
            return True
        return True

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

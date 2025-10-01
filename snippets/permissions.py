from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permissions to allow only an owner of the object
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to GET, HEADER, Options etc
        if request.method in permissions.SAFE_METHODS:
            return True

        # If not safe methods, then check for object ownership
        return obj.owner == request.user

from rest_framework import permissions

class IsAuthenticatedOrCreateOnly(permissions.BasePermission):
    """
    Custom permission to allow anonymous users to create a user.
    """

    def has_permission(self, request, view):
        # Allow all POST requests
        if request.method == 'POST':
            return True

        # Allow authenticated users to access all other methods
        return request.user and request.user.is_authenticated

class IsUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user

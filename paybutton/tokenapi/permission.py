from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    """
    This class inherits the BasePermission class
    from rest_framework permission to create a custom
    permission for authenticated users

    """
    def has_permission(self, request, view):
        if 'username' in request.session:
            return True
        else:
            return False
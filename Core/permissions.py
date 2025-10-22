from rest_framework.permissions import BasePermission

def get_user_group_names(user):
    """Cache group names for the user to avoid repeated DB queries."""
    if not hasattr(user, '_cached_group_names'):
        user._cached_group_names = set(
            user.groups.values_list('name', flat=True)
        )
    return user._cached_group_names



class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        groups = get_user_group_names(request.user)
        return 'Staff' in groups


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        groups = get_user_group_names(request.user)
        return 'Owner' in groups


class IsOwnerOrStaff(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        groups = get_user_group_names(request.user)
        return 'Owner' in groups or 'Staff' in groups

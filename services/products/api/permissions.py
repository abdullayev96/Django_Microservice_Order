from rest_framework.permissions import BasePermission


class HasAuthIDPermission(BasePermission):
    def has_permission(self, request, view):
        return request.META.get("HTTP_AUTH_ID") == "MY155"



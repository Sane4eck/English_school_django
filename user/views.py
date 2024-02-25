from rest_framework import permissions, serializers
from rest_framework import viewsets
from rest_framework.permissions import BasePermission

from user.models import User
from user.serializer import UserSerializer


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action == "create":
            # return [CustomPermission().has_permission(self.request,UserApiViewSet)]
            return [permissions.AllowAny()]
        elif self.action == "partial_update":
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    # def perform_create(self, serializer):
    #     serializer.save()
    #
    # def perform_update(self, serializer):
    #     serializer.save()
    #
    # def perform_destroy(self, instance):
    #     instance.delete()

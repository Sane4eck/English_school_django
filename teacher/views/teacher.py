from rest_framework import viewsets, permissions
from teacher.models import Teacher

from teacher.serializer import (
    TeacherSerializer,
    TestTeacherSerializer,
)


class TeacherModelViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post"]


class TestTeacherModelViewSet(viewsets.ModelViewSet):
    serializer_class = TestTeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get"]

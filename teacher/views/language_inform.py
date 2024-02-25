from rest_framework import viewsets, permissions
from teacher.models import LanguageInform

from teacher.serializer import (
    LanguageInformSerializer,
    TestLanguageInformSerializer,
)


class LanguageInformModelViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageInformSerializer
    queryset = LanguageInform.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post"]


class TestLanguageInformModelViewSet(viewsets.ModelViewSet):
    serializer_class = TestLanguageInformSerializer
    queryset = LanguageInform.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get"]

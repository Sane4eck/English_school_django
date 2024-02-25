# from rest_framework import viewsets, permissions
# from teacher.models import Teacher, LanguageInform
#
# from teacher.serializer import (
#     LanguageInformSerializer,
#     TestLanguageInformSerializer,
#     TeacherSerializer,
#     TestTeacherSerializer,
# )
#
#
# class TeacherModelViewSet(viewsets.ModelViewSet):
#     serializer_class = TeacherSerializer
#     queryset = Teacher.objects.all()
#     permission_classes = [permissions.IsAuthenticated]
#     http_method_names = ["post"]
#
#
# class TestTeacherModelViewSet(viewsets.ModelViewSet):
#     serializer_class = TestTeacherSerializer
#     queryset = Teacher.objects.all()
#     permission_classes = [permissions.AllowAny]
#     http_method_names = ["get"]
#
#
# class LanguageInformModelViewSet(viewsets.ModelViewSet):
#     serializer_class = LanguageInformSerializer
#     queryset = LanguageInform.objects.all()
#     permission_classes = [permissions.IsAuthenticated]
#     http_method_names = ["post"]
#
#
# class TestLanguageInformModelViewSet(viewsets.ModelViewSet):
#     serializer_class = TestLanguageInformSerializer
#     queryset = LanguageInform.objects.all()
#     permission_classes = [permissions.AllowAny]
#     http_method_names = ["get"]

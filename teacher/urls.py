from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teacher.views import (
    TeacherModelViewSet,
    LanguageInformModelViewSet,
    TestLanguageInformModelViewSet,
    TestTeacherModelViewSet,
)

router = DefaultRouter()
router.register("about_test", TestTeacherModelViewSet, basename="TeacherAll")
router.register("about", TeacherModelViewSet, basename="Teacher")
router.register(
    "language_inform_test", TestLanguageInformModelViewSet, basename="LanguageInformAll"
)
router.register(
    "language_inform", LanguageInformModelViewSet, basename="LanguageInform"
)

urlpatterns = []  # path("", include(router.urls)),
urlpatterns += router.urls

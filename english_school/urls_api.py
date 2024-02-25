from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("user/", include("user.urls")),
    path("authorization/", include("authorization.urls")),
    path("confirmation_email/", include("confirmation_email.urls")),
    path("teacher/", include("teacher.urls")),
]

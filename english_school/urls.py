from django.contrib import admin
from django.urls import path, include

from english_school import urls_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(urls_api)),
]

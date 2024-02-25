from django.urls import path, include
from rest_framework.routers import DefaultRouter
from confirmation_email.views import (
    ConfirmationEmailApiView,
    ConfirmationEmailRefreshApiView,
    TestConfirmationToken,
)

router = DefaultRouter()
router.register("email_status", ConfirmationEmailApiView, basename="email_status")
router.register(
    "test_confirmation_token", TestConfirmationToken, basename="test_confirmation_token"
)

urlpatterns = [
    path(
        "email_status_refresh/",
        ConfirmationEmailRefreshApiView.as_view(),
        name="email_status_refresh",
    ),
]
urlpatterns += router.urls

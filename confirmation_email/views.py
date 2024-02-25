from datetime import datetime
from django.utils import timezone
from rest_framework import status, viewsets, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from confirmation_email.models import ConfirmationEmail
from rest_framework.response import Response

from confirmation_email.serializer import ConfirmationSenderEmailSerializer
from utils.email_sender.user_confirmation_email import ConfirmationEmailSender
from user.models import User


def time():
    return datetime.utcnow()


class ConfirmationEmailApiView(RetrieveModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    lookup_field = "email_confirmation_token"  # изменения ретрив параметра

    def get_queryset(self):
        return ConfirmationEmail.objects.filter(date_finish__gt=timezone.now())

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.status_email = True
        instance.user.save()
        instance.delete()
        return Response({"status": True})


class ConfirmationEmailRefreshApiView(CreateModelMixin, GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        json_data = request.data
        instance = User.objects.filter(email=json_data["email"]).first()
        if not instance:
            return Response({"There is no such email": status.HTTP_404_NOT_FOUND})
        if instance.status_email:
            return Response({"Email already confirmed": status.HTTP_200_OK})
        else:
            confirmation_email, created = ConfirmationEmail.objects.get_or_create(
                user=instance, defaults={}
            )
            if confirmation_email.date_finish < timezone.now():
                confirmation_email.update_token()
                ConfirmationEmailSender(to_email=instance.email).send_email(
                    user=instance, email_confirmation_token=confirmation_email
                )
            else:
                return Response(
                    {"detail": "The letter is already in your mail, check your spam"}
                )
            return Response({"detail": "A letter has been sent by mail"})


class TestConfirmationToken(viewsets.ModelViewSet):
    serializer_class = ConfirmationSenderEmailSerializer
    queryset = ConfirmationEmail.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get"]

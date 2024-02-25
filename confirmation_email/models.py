import uuid
from datetime import timedelta, datetime
from django.utils import timezone
from django.db import models
from user.models import User


def time_end():
    return timezone.now() + timedelta(hours=24)  # TODO minutes=5)


class ConfirmationEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    date_finish = models.DateTimeField(default=time_end)

    def update_token(self):
        self.email_confirmation_token = uuid.uuid4()
        self.date_finish = time_end()
        self.save()

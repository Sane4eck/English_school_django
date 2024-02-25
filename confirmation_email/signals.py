from django.db.models.signals import post_save
from django.dispatch import receiver

from confirmation_email.models import ConfirmationEmail
from utils.email_sender.user_confirmation_email import ConfirmationEmailSender


@receiver(post_save, sender=ConfirmationEmail)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:
        ConfirmationEmailSender(to_email=instance.user.email).send_email(
            user=instance.user,
            email_confirmation_token=ConfirmationEmail.objects.get(user=instance.user),
        )

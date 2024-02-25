from confirmation_email.models import ConfirmationEmail
from confirmation_email.serializer import ConfirmationSenderEmailSerializer
from utils.email_sender.base_utils import EmailSender


class ConfirmationEmailSender(EmailSender):
    email = "email/confirmation_email.html"
    subject = "English_site"

    def generate_context(self, **kwargs):
        user = kwargs["user"]
        return ConfirmationSenderEmailSerializer(
            ConfirmationEmail.objects.get(user_id=user.id)
        ).data

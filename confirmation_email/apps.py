from django.apps import AppConfig


class ConfirmationEmailConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "confirmation_email"

    def ready(self):
        import confirmation_email.signals

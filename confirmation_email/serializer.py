from rest_framework import serializers

from confirmation_email.models import ConfirmationEmail


class ConfirmationSenderEmailSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name")

    verification_url = serializers.SerializerMethodField()

    def get_verification_url(self, obj):
        return f"http://127.0.0.1:8000/api/confirmation_email/email_status/{obj.email_confirmation_token}/"

    class Meta:
        model = ConfirmationEmail
        fields = ["user_name", "verification_url"]

from datetime import datetime, timedelta

from rest_framework import serializers

from confirmation_email.models import ConfirmationEmail

from user.models import User


def time_end():
    return datetime.utcnow() + timedelta(hours=24)  # TODO minutes=5)


class CustomPermission:
    def custom_permission(self, context):
        user_permission = context["request"].user
        if user_permission.is_authenticated:
            raise serializers.ValidationError(
                "Вы уже авторизованы и не можете создать новый аккаунт."
            )
        return None


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "second_name",
            "email",
            "password",
            "number_phone",
            "date_registration",
            "gender",
            "birthday",
            "role",
            "status_email",
        ]

    def create(self, validated_data):
        CustomPermission().custom_permission(self.context)
        user = User.objects.create_user(**validated_data)
        ConfirmationEmail.objects.create(
            user=user,
        )
        # ConfirmationEmailSender(to_email=user.email).send_email(
        #     user=user, email_confirmation_token=confirmation_email
        # )
        return user

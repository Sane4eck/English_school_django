from rest_framework import serializers

# from utils.email_sender.teacher_approval import TeacherRequestApprovalSender
# from english_school.settings import EMAIL_HOST_USER
from teacher.models import LanguageInform


class LanguageInformSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs["teacher"] = self.context["request"].user.teacher
        return attrs

    def create(self, validated_data):  # TODO signal
        language_inform = super().create(validated_data)
        # TeacherRequestApprovalSender(to_email=EMAIL_HOST_USER).send_email(
        #     language_inform=language_inform
        # )
        return language_inform

    class Meta:
        model = LanguageInform
        fields = ["language", "cost", "experience_language"]


class TeacherApprovalSendEmailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="teacher.user.name")
    second_name = serializers.CharField(source="teacher.user.second_name")
    email = serializers.CharField(source="teacher.user.email")
    number_phone = serializers.CharField(source="teacher.user.number_phone")
    date_registration = serializers.CharField(source="teacher.user.date_registration")
    gender = serializers.CharField(source="teacher.user.gender")
    birthday = serializers.CharField(source="teacher.user.birthday")
    role = serializers.CharField(source="teacher.user.role")
    about_teacher = serializers.CharField(source="teacher.about_teacher")

    reset_url = serializers.SerializerMethodField()

    def get_reset_url(self, obj):
        return f"http://127.0.0.1:8000/admin/teacher/languageinform/{obj.id}/change/"

    class Meta:
        model = LanguageInform
        fields = [
            "username",
            "second_name",
            "email",
            "number_phone",
            "date_registration",
            "gender",
            "birthday",
            "role",
            "about_teacher",
            "language",
            "cost",
            "experience_language",
            "reset_url",
        ]


# {
#             "username": user.name,
#             "second_name": user.second_name,
#             "email": user.email,
#             "number_phone": user.number_phone,
#             "date_registration": user.date_registration,
#             "gender": user.gender,
#             "birthday": user.birthday,
#             "role": user.role,
#             "about_teacher": teacher.about_teacher,
#             "language": language_inform.language,
#             "cost": language_inform.cost,
#             "experience_language": language_inform.experience_language,
#             "reset_url": f"http://127.0.0.1:8000/admin/teacher/languageinform/{language_inform.id}/change/",
#         }


class TestLanguageInformSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageInform
        fields = "__all__"

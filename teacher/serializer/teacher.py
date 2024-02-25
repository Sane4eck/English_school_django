from rest_framework import serializers

from teacher.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs["user"] = self.context["request"].user
        return attrs

    class Meta:
        model = Teacher
        fields = ["about_teacher"]


class TestTeacherSerializer(serializers.ModelSerializer):
    test_field = serializers.SerializerMethodField()

    def get_test_field(self, obj):
        return f"{obj.user.name} abcd"

    test_field_2 = serializers.CharField(source="user.name")

    class Meta:
        model = Teacher
        fields = ["about_teacher", "test_field_2", "test_field"]

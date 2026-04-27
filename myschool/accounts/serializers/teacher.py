from rest_framework import serializers
from accounts.models.teacher import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = [
            "id",
            "user_id",
            "user",
            "speciality",
            "phone_number",
            "gender",
            "address",
            "image",
        ]

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "email": obj.user.email,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
        }
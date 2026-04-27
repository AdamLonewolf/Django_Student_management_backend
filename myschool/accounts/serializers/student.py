from rest_framework import serializers
from accounts.models.student import Student


class StudentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "id",
            "user_id",
            "user",
            "level_id",
            "level",
            "birthdate",
            "gender",
            "phone_number",
            "student_number",
            "image",
            "address",
        ]

   
    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "email": obj.user.email,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
        }

    def get_level(self, obj):
        if obj.level:
            return {
                "id": obj.level.id,
                "name": obj.level.name,
                "field": obj.level.field.name,
            }
        return None
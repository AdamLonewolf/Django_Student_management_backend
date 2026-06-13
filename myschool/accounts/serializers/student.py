from rest_framework import serializers
from accounts.models.student import Student
from academics.models.level import Level

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    student_number = serializers.CharField(required=False, read_only=True)
    level_id = serializers.PrimaryKeyRelatedField(
        queryset=Level.objects.all(),
        source='level',
        allow_null=True,
        required=False
    )

    class Meta:
        model = Student
        fields = [
            "id", "user_id", "user", "level_id", "level",
            "birthdate", "gender", "phone_number",
            "student_number", "image", "address",
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
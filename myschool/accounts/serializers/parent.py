from rest_framework import serializers
from accounts.models.parent import Parent


class ParentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()

    class Meta:
        model = Parent
        fields = [
            "id",
            "user_id",
            "user",
            "phone_number",
            "address",
            "parent_type",
            "students",
        ]

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "email": obj.user.email,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
        }

  
    def get_students(self, obj):
        return [
            {
                "id": student.id,
                "first_name": student.user.first_name,
                "last_name": student.user.last_name,
                "student_number": student.student_number,
            }
            for student in obj.students.all()
        ]
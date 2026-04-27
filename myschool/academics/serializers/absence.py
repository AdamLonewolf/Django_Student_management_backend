from rest_framework import serializers
from academics.models.absence import Absence


class AbsenceSerializer(serializers.ModelSerializer):

    student = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()

    class Meta:
        model = Absence
        fields = [
            "id",
            "student_id",
            "student",
            "course_id",
            "course",
            "date",
            "justified",
            "reason",
            "created_at"
        ]

    def get_student(self, obj):
        return {
            "id": obj.student.id,
            "first_name": obj.student.user.first_name,
            "last_name": obj.student.user.last_name,
        }

    def get_course(self, obj):
        return {
            "id": obj.course.id,
            "name": obj.course.name,
        }
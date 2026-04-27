from rest_framework import serializers
from academics.models.enrollment import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):

    student = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student_id",
            "student",
            "course_id",
            "course",
            "status",
            "enrolled_at"
        ]

    def get_student(self, obj):
        return {
            "id": obj.student.id,
            "first_name": obj.student.user.first_name,
            "last_name": obj.student.user.last_name,
            "student_number": obj.student.student_number,
        }

    def get_course(self, obj):
        return {
            "id": obj.course.id,
            "name": obj.course.name,
        }
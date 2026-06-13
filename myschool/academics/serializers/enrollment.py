from rest_framework import serializers
from academics.models.enrollment import Enrollment
from accounts.models.student import Student
from academics.models.course import Course

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student'
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='course'
    )

    class Meta:
        model = Enrollment
        fields = ["id", "student_id", "student", "course_id", "course", "status", "enrolled_at"]

    def get_student(self, obj):
        return {
            "id": obj.student.id,
            "first_name": obj.student.user.first_name,
            "last_name": obj.student.user.last_name,
            "student_number": obj.student.student_number,
        }

    def get_course(self, obj):
        return {"id": obj.course.id, "name": obj.course.name}
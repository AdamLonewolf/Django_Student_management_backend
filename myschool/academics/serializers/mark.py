from rest_framework import serializers
from academics.models.mark import Mark


class MarkSerializer(serializers.ModelSerializer):

    enrollment = serializers.SerializerMethodField()

    class Meta:
        model = Mark
        fields = ["id", "enrollment_id", "enrollment", "mark", "remark", "graded_at"]

    def get_enrollment(self, obj):
        return {
            "id": obj.enrollment.id,
            "student": obj.enrollment.student.user.first_name + " " + obj.enrollment.student.user.last_name,
            "course": obj.enrollment.course.name,
        }
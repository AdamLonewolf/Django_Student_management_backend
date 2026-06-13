from rest_framework import serializers
from assignments.models.assignment import Assignment
from academics.models.course import Course

class AssignmentSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='course'
    )

    class Meta:
        model = Assignment
        fields = ["id", "course_id", "course", "title", "description", "due_date", "created_at"]

    def get_course(self, obj):
        return {"id": obj.course.id, "name": obj.course.name}
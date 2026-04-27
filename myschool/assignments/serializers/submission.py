from rest_framework import serializers
from assignments.models.submission import Submission


class SubmissionSerializer(serializers.ModelSerializer):

    assignment = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = [
            "id",
            "assignment_id",
            "assignment",
            "student_id",
            "student",
            "submitted_at",
        ]

    def get_assignment(self, obj):
        return {
            "id": obj.assignment.id,
            "title": obj.assignment.title,
        }

    def get_student(self, obj):
        return {
            "id": obj.student.id,
            "first_name": obj.student.user.first_name,
            "last_name": obj.student.user.last_name,
        }
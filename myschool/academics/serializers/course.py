from rest_framework import serializers
from academics.models.course import Course
from accounts.models.teacher import Teacher

class CourseSerializer(serializers.ModelSerializer):

    teacher = serializers.SerializerMethodField()
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        source='teacher',
        allow_null=True,
        required=False
    )

    class Meta:
        model = Course
        fields = ["id", "name", "description", "teacher_id", "teacher", "created_at"]

    def get_teacher(self, obj):
        if obj.teacher:
            return {
                "id": obj.teacher.id,
                "first_name": obj.teacher.user.first_name,
                "last_name": obj.teacher.user.last_name,
            }
        return None
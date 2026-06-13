from rest_framework import serializers
from academics.models.schedule import Schedule
from academics.models.course import Course

class ScheduleSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='course'
    )

    class Meta:
        model = Schedule
        fields = ["id", "course_id", "course", "day", "start_time", "end_time", "room"]

    def get_course(self, obj):
        teacher = None
        if obj.course.teacher:
            teacher = f"{obj.course.teacher.user.first_name} {obj.course.teacher.user.last_name}"
        return {
            "id": obj.course.id,
            "name": obj.course.name,
            "teacher": teacher or "—"
        }
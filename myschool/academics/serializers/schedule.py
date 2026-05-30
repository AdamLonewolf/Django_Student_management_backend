# academics/serializers/schedule.py
from rest_framework import serializers
from academics.models.schedule import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ["id", "course_id", "course", "day", "start_time", "end_time", "room"]

    def get_course(self, obj):
        return {
            "id": obj.course.id,
            "name": obj.course.name,
            "teacher": f"{obj.course.teacher.user.first_name} {obj.course.teacher.user.last_name}" if obj.course.teacher else "—"
        }
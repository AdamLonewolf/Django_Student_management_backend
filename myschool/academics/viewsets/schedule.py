# academics/viewsets/schedule.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from academics.models.schedule import Schedule
from academics.serializers.schedule import ScheduleSerializer
from accounts.permissions import IsAdmin

class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Schedule.objects.none()

        user = self.request.user

        if user.role == 'teacher':
            return Schedule.objects.filter(
                course__teacher__user=user
            )
        if user.role == 'student':
            return Schedule.objects.filter(
                course__enrollments__student__user=user
            ).distinct()
        if user.role == 'parent':
            return Schedule.objects.filter(
                course__enrollments__student__parents__user=user
            ).distinct()

        return Schedule.objects.all()
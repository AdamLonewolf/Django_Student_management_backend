from rest_framework.viewsets import ModelViewSet
from assignments.models.assignment import Assignment
from assignments.serializers.assignment import AssignmentSerializer
from accounts.permissions import IsAdminOrTeacher
from rest_framework.permissions import IsAuthenticated


class AssignmentViewSet(ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrTeacher()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return Assignment.objects.filter(
                course__enrollments__student__user=user
            )
        if user.role == 'teacher':
            return Assignment.objects.filter(course__teacher__user=user)
        return Assignment.objects.all()
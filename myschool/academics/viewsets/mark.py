from rest_framework.viewsets import ModelViewSet
from academics.models.mark import Mark
from academics.serializers.mark import MarkSerializer
from accounts.permissions import IsAdminOrTeacher, IsStudent
from rest_framework.permissions import IsAuthenticated


class MarkViewSet(ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrTeacher()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return Mark.objects.filter(enrollment__student__user=user)
        if user.role == 'teacher':
            return Mark.objects.filter(enrollment__course__teacher__user=user)
        return Mark.objects.all()
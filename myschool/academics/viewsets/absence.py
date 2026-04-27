from rest_framework.viewsets import ModelViewSet
from academics.models.absence import Absence
from academics.serializers.absence import AbsenceSerializer
from accounts.permissions import IsAdminOrTeacher
from rest_framework.permissions import IsAuthenticated


class AbsenceViewSet(ModelViewSet):
    serializer_class = AbsenceSerializer
    queryset = Absence.objects.all()
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrTeacher()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return Absence.objects.filter(student__user=user)
        if user.role == 'teacher':
            return Absence.objects.filter(course__teacher__user=user)
        return Absence.objects.all()
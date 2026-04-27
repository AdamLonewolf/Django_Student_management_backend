from rest_framework.viewsets import ModelViewSet
from assignments.models.submission import Submission
from assignments.serializers.submission import SubmissionSerializer
from accounts.permissions import IsAdminOrTeacher, IsStudent
from rest_framework.permissions import IsAuthenticated


class SubmissionViewSet(ModelViewSet):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all() 
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAdminOrTeacher()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return Submission.objects.filter(student__user=user)
        if user.role == 'teacher':
            return Submission.objects.filter(
                assignment__course__teacher__user=user
            )
        return Submission.objects.all()
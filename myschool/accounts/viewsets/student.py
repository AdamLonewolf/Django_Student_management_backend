from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from accounts.models.student import Student
from accounts.serializers.student import StudentSerializer
from accounts.permissions import IsAdminOrTeacher, IsAdmin

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAdminOrTeacher()]
        return [IsAdmin()]

    def get_queryset(self):  # ← indenté à l'intérieur
        user = self.request.user
        
        if getattr(self, 'swagger_fake_view', False):
            return Student.objects.none()
        
        if user.role == 'student':
            return Student.objects.filter(user=user)
        
        if user.role == 'teacher':
            return Student.objects.filter(
                enrollments__course__teacher__user=user
            ).distinct()
        
        if user.role == 'parent':
            return Student.objects.filter(
                parents__user=user
            )
        
        return Student.objects.all()
    
    
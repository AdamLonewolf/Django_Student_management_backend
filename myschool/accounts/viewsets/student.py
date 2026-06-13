import uuid
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
            return [IsAuthenticated()]  
        return [IsAdmin()]

    def perform_create(self, serializer):
        from accounts.models.user import User
        user = User.objects.create_user(
            email=self.request.data.get('email'),
            first_name=self.request.data.get('first_name'),
            last_name=self.request.data.get('last_name'),
            role='student',
            password=self.request.data.get('password')
        )
        
        student_number = f"STU-{uuid.uuid4().hex[:8].upper()}"
        serializer.save(user=user, student_number=student_number)

    def perform_update(self, serializer):
        instance = serializer.save()
        password = self.request.data.get('password')
        if password:
            instance.user.set_password(password)
            instance.user.save()

    def perform_destroy(self, instance):
        user = instance.user  
        instance.delete()     
        user.delete()        

    def get_queryset(self):
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
            return Student.objects.filter(parents__user=user)

        return Student.objects.all()
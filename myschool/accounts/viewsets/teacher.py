from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from accounts.models.teacher import Teacher
from accounts.serializers.teacher import TeacherSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        from accounts.models.user import User
        user = User.objects.create_user(
            email=self.request.data.get('email'),
            first_name=self.request.data.get('first_name'),
            last_name=self.request.data.get('last_name'),
            role='teacher',
            password=self.request.data.get('password')
        )
        serializer.save(user=user)

    def perform_update(self, serializer):
        instance = serializer.save()
        password = self.request.data.get('password')
        if password:
            instance.user.set_password(password)
            instance.user.save()
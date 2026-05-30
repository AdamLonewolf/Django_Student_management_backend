from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from accounts.models.parent import Parent
from accounts.serializers.parent import ParentSerializer


class ParentViewSet(ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        from accounts.models.user import User
        user = User.objects.create_user(
            email=self.request.data.get('email'),
            first_name=self.request.data.get('first_name'),
            last_name=self.request.data.get('last_name'),
            role='parent',
            password=self.request.data.get('password')
        )
        serializer.save(user=user)

    def perform_update(self, serializer):
        instance = serializer.save()
        password = self.request.data.get('password')
        if password:
            instance.user.set_password(password)
            instance.user.save()
from rest_framework import serializers
from accounts.models.teacher import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = [
            "id",
            "user_id",
            "user",
            "speciality",
            "phone_number",
            "gender",
            "address",
            "image",
        ]
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

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "email": obj.user.email,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
        }
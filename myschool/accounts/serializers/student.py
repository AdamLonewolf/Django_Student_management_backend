from rest_framework import serializers
from accounts.models.student import Student


class StudentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "id",
            "user_id",
            "user",
            "level_id",
            "level",
            "birthdate",
            "gender",
            "phone_number",
            "student_number",
            "image",
            "address",
        ]
    
        def perform_create(self, serializer):
            user_data = {
                'email': self.request.data.get('email'),
                'first_name': self.request.data.get('first_name'),
                'last_name': self.request.data.get('last_name'),
                'role': 'student',
            }
            from accounts.models.user import User
            user = User.objects.create_user(**user_data, password=self.request.data.get('password'))
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

    def get_level(self, obj):
        if obj.level:
            return {
                "id": obj.level.id,
                "name": obj.level.name,
                "field": obj.level.field.name,
            }
        return None
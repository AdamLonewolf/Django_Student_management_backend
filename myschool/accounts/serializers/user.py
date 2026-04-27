from rest_framework import serializers
from accounts.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "role",
            "is_active",
            "created_at",
        ]
        # arguments supplémentaire pour que le mdp n'apparaisse pas dans la bdd.
        extra_kwargs = {
            'password': {'write_only': True}
        }
from rest_framework import serializers
from academics.models.field import Field


class FieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = ["id", "name", "description", "created_at"]
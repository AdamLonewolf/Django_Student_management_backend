from rest_framework import serializers
from academics.models.level import Level


class LevelSerializer(serializers.ModelSerializer):

    field = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = ["id", "name", "field_id", "field", "created_at"]

    def get_field(self, obj):
        return {
            "id": obj.field.id,
            "name": obj.field.name,
        }
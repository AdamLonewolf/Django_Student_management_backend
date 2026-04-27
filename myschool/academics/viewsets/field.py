from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from academics.models.field import Field
from academics.serializers.field import FieldSerializer


class FieldViewSet(ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]
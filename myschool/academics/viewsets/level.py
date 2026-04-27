from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from academics.models.level import Level
from academics.serializers.level import LevelSerializer


class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [IsAuthenticated]
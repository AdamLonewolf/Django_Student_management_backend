from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from academics.models.enrollment import Enrollment
from academics.serializers.enrollment import EnrollmentSerializer


class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
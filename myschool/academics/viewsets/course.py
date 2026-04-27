from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from academics.models.course import Course
from academics.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
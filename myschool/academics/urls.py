from rest_framework.routers import DefaultRouter
from django.urls import path, include
from academics.viewsets.field import FieldViewSet
from academics.viewsets.level import LevelViewSet
from academics.viewsets.course import CourseViewSet
from academics.viewsets.enrollment import EnrollmentViewSet
from academics.viewsets.mark import MarkViewSet
from academics.viewsets.absence import AbsenceViewSet

router = DefaultRouter()
router.register(r"fields",      FieldViewSet)
router.register(r"levels",      LevelViewSet)
router.register(r"courses",     CourseViewSet)
router.register(r"enrollments", EnrollmentViewSet)
router.register(r"marks",       MarkViewSet)
router.register(r"absences",    AbsenceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
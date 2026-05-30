from rest_framework.routers import DefaultRouter
from django.urls import path, include
from academics.viewsets.field import FieldViewSet
from academics.viewsets.level import LevelViewSet
from academics.viewsets.course import CourseViewSet
from academics.viewsets.enrollment import EnrollmentViewSet
from academics.viewsets.mark import MarkViewSet
from academics.viewsets.absence import AbsenceViewSet
from academics.viewsets.schedule import ScheduleViewSet
from academics.views.bulletin import BulletinView

router = DefaultRouter()
router.register(r"fields",      FieldViewSet)
router.register(r"levels",      LevelViewSet)
router.register(r"courses",     CourseViewSet)
router.register(r"enrollments", EnrollmentViewSet)
router.register(r"marks",       MarkViewSet)
router.register(r"absences",    AbsenceViewSet)
router.register(r"schedules", ScheduleViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("students/<int:student_id>/bulletin/", BulletinView.as_view(), name="bulletin"),
]
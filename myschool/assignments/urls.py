from rest_framework.routers import DefaultRouter
from django.urls import path, include
from assignments.viewsets.assignment import AssignmentViewSet
from assignments.viewsets.submission import SubmissionViewSet

router = DefaultRouter()
router.register(r"assignments", AssignmentViewSet)
router.register(r"submissions", SubmissionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
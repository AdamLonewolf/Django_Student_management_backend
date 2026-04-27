from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
from accounts.viewsets.user import UserViewSet
from accounts.viewsets.student import StudentViewSet
from accounts.viewsets.teacher import TeacherViewSet
from accounts.viewsets.parent import ParentViewSet
from accounts.views.auth import RegisterView, LoginView, LogoutView

router = DefaultRouter()
router.register(r"users",    UserViewSet)
router.register(r"students", StudentViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"parents",  ParentViewSet)


#Authentification

urlpatterns = [
    path("", include(router.urls)),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"), # Pour le login 
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), # Refresh du token
    path("auth/logout/", LogoutView.as_view(), name="logout"), #Blacklist le refresh token
]
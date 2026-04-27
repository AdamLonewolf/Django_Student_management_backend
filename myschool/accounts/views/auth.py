from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models.user import User


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email      = request.data.get('email')
        password   = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name  = request.data.get('last_name')
        role       = request.data.get('role', 'student')

    
        if not email or not password or not first_name or not last_name:
            return Response(
                {"error": "Tous les champs sont obligatoires"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Cet email existe déjà"},
                status=status.HTTP_400_BAD_REQUEST
            )

        
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role,
        )

        # Génère les tokens 
        refresh = RefreshToken.for_user(user)

        return Response({
            "access":  str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id":         user.id,
                "email":      user.email,
                "first_name": user.first_name,
                "last_name":  user.last_name,
                "role":       user.role,
            }
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):

    permission_classes = [AllowAny]  

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')


        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response(
                {"error": "Email ou mot de passe incorrect"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        
        refresh = RefreshToken.for_user(user)

        return Response({
            "access":  str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id":         user.id,
                "email":      user.email,
                "first_name": user.first_name,
                "last_name":  user.last_name,
                "role":       user.role,
            }
        })
    

class LogoutView(APIView):

    permission_classes = [IsAuthenticated]  # faut être connecté pour logout

    def post(self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response(
                {"error": "Refresh token manquant"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Blackliste le refresh token
        # → même si quelqu'un le vole, il ne peut plus l'utiliser
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response(
            {"message": "Déconnexion réussie"},
            status=status.HTTP_200_OK
        )
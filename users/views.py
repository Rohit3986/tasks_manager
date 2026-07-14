from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


from .models import UserProfile
from .serializers import UserProfileSerializer, LoginSerializer


class LoginView(APIView):
    """Login endpoint. Returns an auth token for valid credentials."""

    permission_classes = [AllowAny]


    @extend_schema(
        request=LoginSerializer,
        responses={200: {"type": "object", "properties": {
            "token": {"type": "string"}
        }}},
        summary="Login User",
        description="Authenticate user and return auth token."
    )

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"detail": "username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)
        if user is None:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class ProfileView(APIView):
    def get(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

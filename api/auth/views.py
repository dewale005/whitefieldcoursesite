from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import RegisterationSerializers, LoginSerializer

User = get_user_model()

class RegisterUser(generics.CreateAPIView):
    query_set = User.objects.all()
    serializer_class = RegisterationSerializers
    permission_class = [permissions.AllowAny]


class LoginUser(ObtainAuthToken):
    serializer_class = LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
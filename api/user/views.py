from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UsersSerializers

User = get_user_model()

class Profile(generics.RetrieveUpdateDestroyAPIView):
    query_set = User.objects.all()
    serializer_class = UsersSerializers
    # permission_class = [permissions.AllowAny]
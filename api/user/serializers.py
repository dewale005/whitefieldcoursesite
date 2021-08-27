from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()

class UsersSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        

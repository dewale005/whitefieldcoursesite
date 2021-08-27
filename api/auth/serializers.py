from django.contrib.auth import get_user_model, authenticate
from django.db.models import fields
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterationSerializers(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False, allow_blank=True, allow_null=True, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password', 'token',)
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5}, 
            'first_name': {'write_only': True}, 
            'last_name': {'write_only': True}, 
            'email': {'write_only': True}, 
            'phone_number': {'write_only': True}, 
            }

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.validationError("User with this email already exist")
        return value

    def validate_phone(self, value):
        qs = User.objects.filter(phone_number__iexact=value)
        if qs.exists():
            raise serializers.validationError("User with this Phone number already exist")
        return value

    def get_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key
        

    def create(self, validated_data):
        """create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
            
        
        return user

class LoginSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False, allow_blank=True, allow_null=True, write_only=True)
    
    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if not user:
            msg = ('Unable to autheticate with provided details')
            raise serializers.ValidationError(msg, code='authetication')

        attrs['user'] = user
        return attrs
import os
import uuid

from django.db import models
from django.conf import settings
from django.utils.timezone import now

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


def document_images_file_path(instance,  filename):
    """Generate file path for images """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('user', filename)

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError('User must have email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.role = 'admin'
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    CHOICES = (
        ('prefer-not-to-say', 'Prefer not to say'),
        ('male', 'Male'),
        ('female', 'Female'),
    )

    LOCATION_CHOICES = (
        ('lagos', 'Lagos State'),
        ('ogun', 'Ogun State'),
        ('oyo', 'Oyo State'),
        ('abuja', 'Abuja (FCT) State'),
        ('rivers', 'Rivers State'),
        ('abia', 'Abia State'),
        ('adamawa', 'Adamawa State'),
        ('akwa-ibon', 'Akwa Ibon State'),
        ('bauchi', 'Bauchi State'),
        ('bayelsa', 'Bayelsa State'),
        ('benue', 'Benue State'),
        ('borno', 'Borno State'),
        ('cross-rivers', 'Cross Rivers State'),
        ('deltaz', 'Delta State'),
        ('ebonyi', 'Ebonyi State'),
        ('edo', 'Edo State'),
        ('ekitiz', 'Ekiti State'),
        ('enugu', 'Enugu State'),
        ('gombe', 'Gombe State'),
        ('imo', 'Imo State'),
        ('jigawa', 'Jigawa State'),
        ('kaduna', 'Kaduna State'),
        ('kano', 'Kano State'),
        ('katsina', 'Katsina State'),
        ('kebbi', 'Kebbi State'),
        ('kogi', 'Kogi State'),
        ('kwara', 'Kwara State'),
        ('nasarawa', 'Nasarawa State'),
        ('niger', 'Niger State'),
        ('ondo', 'Ondo State'),
        ('plateau', 'Sokoto State'),
        ('sokoto', 'Plateau State'),
        ('taraba', 'Taraba State'),
        ('yobe', 'Yobe State'),
        ('zamfara', 'Zamfara State'),
    )

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('tutor', 'Tutor'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(max_length=255,unique=True)
    avatar = models.ImageField(null=True, upload_to=document_images_file_path, blank=True,)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=255, default="", choices = CHOICES)
    location = models.CharField(max_length=255, default="", choices = LOCATION_CHOICES,  blank=True)
    role = models.CharField(max_length=255, default="student", choices = ROLE_CHOICES )
    referal_code = models.CharField(max_length=255, default="", blank=True)
    is_phone_number_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(default=now, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

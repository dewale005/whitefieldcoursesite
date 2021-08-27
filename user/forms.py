import os

from django.db.models import fields
from user import models
import uuid

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model();

def document_images_file_path(instance,  filename):
    """Generate file path for images """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('user', filename)


class UpdateProfileForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'gender', 'location', 'referal_code', 'referal_code', 'date_of_birth']
 

    # email = forms.EmailField()
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # phone_number = forms.CharField()
    # forms.ChoiceField
    # gender = forms.CharField(choices = CHOICES)
    # location = forms.CharField(choices = LOCATION_CHOICES,)
    # referal_code = forms.CharField()
    # date_of_birth = forms.DateField()
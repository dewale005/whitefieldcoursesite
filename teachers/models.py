import os
import uuid
from django.db import models

def document_images_file_path(instance,  filename):
    """Generate file path for images """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('teacher', filename)

class TeacherModel(models.Model):
    full_name = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, upload_to=document_images_file_path, blank=True,)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return "/teachers/{id}".format(id=self.id)


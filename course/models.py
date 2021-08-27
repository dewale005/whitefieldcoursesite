import os
import uuid

from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_save
from teachers.models import TeacherModel

from utils.utils import unique_slug_generator

def document_images_file_path(instance,  filename):
    """Generate file path for images """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('course', filename)

class LessonModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    videoUrl = models.URLField(null=True, blank=True)
    duration = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class SectionModel(models.Model):
    title =  models.CharField(max_length=255, blank=True, null=True)
    bio_description = models.TextField(default="hello", null=True)
    lessons = models.ManyToManyField(LessonModel)
    

    def __str__(self):
        return self.title

class CourseManager(models.Manager):

    def get_by_slug(self, slug):
        return self.get_queryset().filter(slug=slug)

class CoursesModel(models.Model):
    CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    title = models.CharField(max_length=255, null=False);
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(null=True, upload_to=document_images_file_path, blank=True,)
    duration = models.CharField(max_length=255, null=False)
    level = models.CharField(max_length=255, choices=CHOICES, blank=True)
    author = models.ForeignKey(TeacherModel, on_delete=CASCADE)
    lectures = models.ManyToManyField(SectionModel)

    objects = CourseManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/courses/{slug}".format(slug=self.slug)

def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever, sender=CoursesModel)


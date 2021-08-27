from django.contrib import admin

from .models import CoursesModel, LessonModel, SectionModel

admin.site.register(CoursesModel)
admin.site.register(LessonModel)
admin.site.register(SectionModel)

# Register your models here.

from django.urls import path

from .views import course_page, CoursesModelList, CoursesModelDetail

urlpatterns = [
    path('', CoursesModelList.as_view(), name='courses'),
    path('<str:slug>', CoursesModelDetail.as_view(), name='coursesdetails'),
]
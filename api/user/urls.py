from django.urls import path

# from .views import course_page
from .views import Profile


urlpatterns = [
    path('users', Profile.as_view(), name='apiprofile'),
]
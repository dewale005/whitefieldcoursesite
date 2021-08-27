from django.urls import path

from .views import StudentDetail

urlpatterns = [
    path('', StudentDetail.as_view(), name='user_profile'),
]
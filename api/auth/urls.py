from django.urls import path

# from .views import course_page
from .views import RegisterUser, LoginUser


urlpatterns = [
    path('register', RegisterUser.as_view(), name='apiregsiter'),
    path('login', LoginUser.as_view(), name='apilogin'),
]
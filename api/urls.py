from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('users/', include('api.user.urls')),
]
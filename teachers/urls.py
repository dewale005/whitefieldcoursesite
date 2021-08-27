from django.urls import path

from .views import TeachersListView, TeachersDetailView

urlpatterns = [
    path('all', TeachersListView.as_view(), name='teachers'),
    path('<int:pk>', TeachersDetailView.as_view(), name='teachers'),
]
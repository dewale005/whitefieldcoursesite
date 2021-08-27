from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import TeacherModel

class TeachersListView(ListView):
    queryset = TeacherModel.objects.all()
    template_name='pages/teachers.html'


class TeachersDetailView(DetailView):
    # queryset = CoursesModel.objects.all()
    template_name='pages/dashboard/tutor/teachers.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TeachersDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
        
    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get('pk')
        return TeacherModel.objects.filter(id=id)
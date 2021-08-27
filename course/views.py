from django.http import request
from django.http.response import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import CoursesModel

class CoursesModelList(ListView):
    queryset = CoursesModel.objects.all()
    template_name='pages/course.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(CoursesModelList, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

class CoursesModelDetail(DetailView):
    # queryset = CoursesModel.objects.all()
    template_name='pages/dashboard/student/course.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CoursesModelDetail, self).get_context_data(*args, **kwargs)
        print(context)
        return context
        
    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        return CoursesModel.objects.get_by_slug(slug)

def course_page(request):
    return render(request, "pages/course.html")
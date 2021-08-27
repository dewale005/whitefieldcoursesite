from django.views import generic
from utils.auth import LoginRequiredMixins

from user.models import User



class StudentDetail(generic.TemplateView):
    template_name= "pages/dashboard/student/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(StudentDetail, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update your profile'
        return context
    
    def get_queryset(self, *arg, **kwargs):
        return self.request.user
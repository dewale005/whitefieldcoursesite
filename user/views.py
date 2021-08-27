from django.http import request
from django.shortcuts import render
from django.views.generic import UpdateView

from .forms import UpdateProfileForms
# Create your views here.


class UpdateProfileViews(UpdateView):
    form_class = UpdateProfileForms
    template = 'pages/dashboard/student/profile.html'
    success_url = '/dashboard'

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateProfileViews, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update your profile'
        return context
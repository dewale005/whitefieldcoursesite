from django.views.generic.detail import DetailView
from utils.auth import LoginRequiredMixins
from django.contrib.auth import authenticate, get_user_model, logout as auth_logout, login
from django.contrib.auth.decorators import login_required
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.contrib.auth.models import update_last_login
from django.views.generic import TemplateView, FormView, CreateView

from django.shortcuts import render, redirect

from user.models import User

from .forms import LoginForm, RegisterForm, VerificationForm
from webapp import forms

class HomePageView(TemplateView):
    template_name = 'pages/home.html'



def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        if login_form.is_valid():
            username = login_form.cleaned_data.get('email_address')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(request.user.is_authenticated)
            if user is not None:
                login(request, user)
                update_last_login(None, user)
                if not user.is_email_verified or not user.is_phone_number_verified:
                    return redirect('/verify')
                
                return redirect('/dashboard')
            else:
                raise ErrorList
        return render(request, "pages/auth/login.html", context)

class RegisterUserView(FormView):
    form_class = RegisterForm
    template_name = "pages/auth/register.html"
    success_url = '/dashboard'

    def form_valid(self, form):
        new_user = get_user_model().objects.create_user(**form.cleaned_data)
        login(self.request, new_user)
        return redirect('/dashboard')


# def register_page(request):
#     register_form = RegisterForm(request.POST or None)
#     context = {
#         "form": register_form
#     }
#     if request.user.is_authenticated:
#         return redirect('/dashboard')
#     else:
#         if register_form.is_valid():
#             print(register_form.cleaned_data)
#             new_user = get_user_model().objects.create_user(**register_form.cleaned_data)
#             login(request, new_user)
#             return redirect('/dashboard')
#         return render(request, "pages/auth/register.html", context)

def verification(request):
    verify_form = VerificationForm(request.POST or None)
    context = {
        "form": verify_form
    }
    if request.user.is_authenticated and request.user.is_email_verified or request.user.is_phone_number_verified:
        return redirect('/dashboard')
    else:
        if verify_form.is_valid():
            print(verify_form.cleaned_data)
            # username = verify_form.cleaned_data.get('one_time_password')
            # password = verify_form.cleaned_data.get('password')
            # user = authenticate(username=username, password=password)
            # print(request.user.is_authenticated)
            # if user is not None:
                # login(request, user)
                # update_last_login(None, user)
                # if not user.is_email_verified or not user.is_phone_number_verified:
                #     return redirect('/verify')
                # print(user.is_email_verified)
                # print(user.is_phone_number_verified)
                # print(user.clean_fields)
                
        #         return redirect('/dashboard')
            # else:
            #     raise ErrorList
        return render(request, "pages/auth/verify.html", context)

def logout(request):
    auth_logout(request)
    return redirect('/login')


# class DashBoardHomeView(LoginRequiredMixins, DetailView):
#     template_name = "pages/dashboard/student/home.html"

#     def get_object(self):
#         return self.request.user
    

def dashboard_page(request):
    if request.user.is_authenticated:
        return render(request, "pages/dashboard/student/home.html", {})
    else:
        return render(request, "pages/dashboard/student/home.html", {})

def dashboard_learnpath(request):
    if request.user.is_authenticated:
        return render(request, "pages/dashboard/student/learnpath.html", {})
    else:
        return redirect('/login')

def dashboard_lesson(request):
    if request.user.is_authenticated:
        return render(request, "pages/dashboard/student/lesson.html", {})
    else:
        return redirect('/login')

def dashboard_course(request):
    if request.user.is_authenticated:
        return render(request, "pages/dashboard/student/course.html", {})
    else:
        return redirect('/login')

# def dashboard_profile(request):
#     if request.user.is_authenticated:
#         return render(request, "pages/dashboard/student/profile.html", {})
#     else:
#         return redirect('/login')


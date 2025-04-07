from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView

import settings
#import settings
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm
from django.urls import reverse, reverse_lazy



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('index')

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        user = get_user_model().objects.get(username=username)
        if user != self.request.user:
            raise reverse_lazy("profile_error")
        return user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"


class ProfileError(TemplateView):
    template_name = 'users/profile_update_error.html'
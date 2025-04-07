from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from pygments.lexer import default

import settings
from .forms import AddPostForm
from .models import PostModel, PictureModel, CategoryModel
from .utils import DataMixin


class HomePage(DataMixin, ListView):
    model = PostModel
    template_name = 'main/mainpage.html'
    context_object_name = 'post'


class MyPageDetail(LoginRequiredMixin, DataMixin, DetailView):
    model = PostModel
    template_name = 'main/mypage.html'
    context_object_name = 'post'
    extra_context = {
        'default_image': settings.DEFAULT_USER_IMAGE
    }

    def get_queryset(self):
        username = self.kwargs.get('username')
        author = get_user_model().objects.get(username=username)
        return PostModel.objects.filter(author=author)

    def get_object(self):
        username = self.kwargs.get('username')
        user = get_user_model().objects.get(username=username)
        return user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')
        user = get_user_model().objects.get(username=username)
        context['author'] = user
        context['post'] = self.get_queryset()
        return context


class ShowPost(DetailView):
    model = PostModel
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


class CategoryPage(DataMixin, ListView):
    model = CategoryModel
    template_name = 'main/category.html'
    context_object_name = 'categories'


class ShowCategory(DataMixin, ListView):
    model = PostModel
    template_name = 'main/mainpage.html'
    context_object_name = 'post'

    def get_queryset(self):
        category_slug = self.kwargs['cat_slug']
        category = CategoryModel.objects.get(slug=category_slug)
        return PostModel.objects.filter(category_id=category.pk)


class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('index')
    permission_required = 'main.add_main'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)



class UpdatePost(UpdateView):
    model = PostModel
    fields = ['title', 'main_picture', 'content', 'category']
    template_name = 'main/update_post.html'
    success_url = reverse_lazy('index')


class DeletePost(DeleteView):
    model = PostModel
    success_url = reverse_lazy('index')
    template_name = 'main/post_confirm_delete.html'


def user_account_page(request):
    s = 1
    return render(request, 'main/userpage.html')


def page_not(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена ;(</h1>")
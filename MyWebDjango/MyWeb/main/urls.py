from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import MyPageDetail, CategoryPage


urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("mypage/<str:username>", MyPageDetail.as_view(), name="mypage"),
    path("post/<slug:post_slug>", views.ShowPost.as_view(), name="post"),
    path("category", CategoryPage.as_view(), name="category"),
    path("category/<slug:cat_slug>", views.ShowCategory.as_view(), name="categories"),
    path("addpost", views.AddPost.as_view(), name="addpost"),
    path("edit/<slug:slug>", views.UpdatePost.as_view(), name="update_post"),
    path("delete/<slug:slug>", views.DeletePost.as_view(), name="delete_post"),
    path("userpage", views.user_account_page, name="userpage"),
]
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import PostModel, PictureModel, CategoryModel

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_picture', 'pub_date', 'category')
    list_display_links = ('id', 'title', 'pub_date')
    list_editable = ('category',)
    ordering = ['id']
    search_fields = ['title', 'cat__name']
    readonly_fields = ['slug']

    @admin.display(description="Главная фотография поста", ordering='content')
    def post_picture(self, post: PostModel):
        if post.main_picture:
            return mark_safe(f"<img src='{post.main_picture.url}' width=100>")
        return "Без фото"



@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ('name', )}
    list_display_links = ('id', 'name')
    ordering = ['id']


@admin.register(PictureModel)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'post')
    list_display_links = ('id', )
    list_editable = ('post',)
    ordering = ['id']

from django.contrib.auth import get_user_model
from django.db import models
from django.template.base import kwarg_re
from pytils.translit import slugify
from django.urls import reverse


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_slug': self.slug})


class PostModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    content = models.TextField(max_length=2500, verbose_name="Контент")
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    main_picture = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True, verbose_name="Картинка")
    category = models.ForeignKey('CategoryModel', on_delete=models.PROTECT)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class PictureModel(models.Model):
    picture = models.ImageField(upload_to="photo/%Y/%m/%d/")
    description = models.CharField(max_length=250, verbose_name="Описание")
    post = models.ForeignKey('PostModel', on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['description']
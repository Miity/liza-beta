import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.conf import settings
from django.views.generic import ListView, DetailView
from .models import Post, Category, Post_Gallery, Inline_Editor


# Create your views here.

class CategoryList:
    def get_category(self):
        if len(Category.objects.all()) >= 1:
            return Category.objects.all()


class Post_by_Cat(ListView, CategoryList):
    model = Post
    template_name = "blog/blog-portfolio.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Post_by_Cat, self).get_context_data(*args, **kwargs)

        if len(Post.objects.filter(category__slug=self.kwargs.get('slug')).filter(status=True)) >= 1:
            context['post_list'] = Post.objects.filter(category__slug=self.kwargs.get('slug')).filter(status=True)
        else:
            context['post_list'] = Post.objects.all()

        return context


class Post_Detail(DetailView):
    model = Post
    slug_field = "slug"

    template_name = "blog/post_detail.html"  # указывать не обязательно!, можно через "model", тогда джагнго

    # будет искатьт шаблон Post_detail.html

    def get_context_data(self, *args, **kwargs):
        context = super(Post_Detail, self).get_context_data(*args, **kwargs)
        post = self.object.id
        context['images'] = Post_Gallery.objects.filter(post=post)
        context['inlinetext'] = Inline_Editor.objects.filter(post=post)
        context['next'] = Post.objects.filter(my_order__gt=self.object.my_order).order_by("my_order").first()
        context['prev'] = Post.objects.filter(my_order__lt=self.object.my_order).order_by("-my_order").first()
        context['ckeditor_config'] = json.dumps(settings.CKEDITOR_CONFIGS["default"])
        return context

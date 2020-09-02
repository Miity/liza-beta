from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import Post, Category


def get_category(self):
    if len(Category.objects.all()) >= 1:
        return Category.objects.all()


def index(request):
    # Функция отображения для домашней страницы сайта.
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'lizabeta/index.html',
        context={'post_list': posts, 'categories': categories,}
    )

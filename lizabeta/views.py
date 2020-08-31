from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import Post, Category


def index(request):
    # Функция отображения для домашней страницы сайта.
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'lizabeta/index.html',
        context={'posts': posts, 'categories': categories}
    )

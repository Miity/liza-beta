from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import Post, Category


def get_category(request):
    if len(Category.objects.all()) >= 1:
        return Category.objects.all()


def index(request):
    # Функция отображения для домашней страницы сайта.
    posts = Post.objects.all()
    categories = get_category(request)

    return render(
        request,
        'blog/blog-portfolio.html',
        context={'post_list': posts, 'categories': categories,}
    )

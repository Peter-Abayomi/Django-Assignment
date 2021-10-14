from django.shortcuts import render, get_object_or_404
from .models import Post, FrontImage


def index(request):
    posts = Post.objects.all()
    images = FrontImage.objects.all()
    context = {
        'posts': posts,
        'images': images,
    }
    return render(request, 'blogs/index.html', context)


def details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blogs/details.html', context)

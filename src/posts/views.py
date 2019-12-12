from django.shortcuts import render
from .models import Post


def index(request):
    """
        Grab only the posts that have featured=True, in future this will be my owl carousel
    """
    featured = Post.objects.filter(featured=True)
    # Grab onny the first 3 posts and the latest, because of negative timestamp
    latest = Post.objects.order_by('-timestamp')[0:3]

    context = {
        'object_list': featured,
        'latest': latest
    }

    return render(request, 'index.html', context)


def blog(request):
    #post_list = Post.objects.all()
    post_list = Post.objects.all().order_by('-timestamp')

    context = {
        'post_list': post_list
    }

    return render(request, 'blog.html', context)


def post(request):
    return render(request, 'post.html', {})

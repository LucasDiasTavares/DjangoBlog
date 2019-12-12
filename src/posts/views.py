from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    post_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(post_list, 8)
    page_request = 'page'
    page = request.GET.get(page_request)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request': page_request
    }

    return render(request, 'blog.html', context)


def post(request):
    return render(request, 'post.html', {})

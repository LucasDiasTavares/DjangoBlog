from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post


def get_category_count():
    # method to see the name and the count of every category
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


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
    category_count = get_category_count()

    # Grab all posts and orderby negative timestamp
    post_list = Post.objects.all().order_by('-timestamp')

    # latest posts
    most_recent = Post.objects.order_by('-timestamp')[0:3]

    # Pagination
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
        'page_request': page_request,
        'most_recent': most_recent,
        'category_count': category_count
    }

    return render(request, 'blog.html', context)


def post(request, id):
    return render(request, 'post.html', {})

from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import Post


# Methods
def get_category_count():
    # Method to see the name and count of every category
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


def get_most_recent_four_posts():
    # Method to get the most recent 4 posts
    most_recent = Post.objects.order_by('-timestamp')[0:4]
    return most_recent


def search(request):
    # Grab all of my posts
    queryset = Post.objects.all()
    # GET parameter from my url, my 'q' needs to be exacly name from your form (name="q")
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            # Filter by title or overview, you can put as many fields you want
            Q(title__icontains=query) |
            Q(categories__title__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }

    return render(request, 'search_results.html', context)


# Pages
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
    # Grab all posts and orderby negative timestamp
    post_list = Post.objects.all().order_by('-timestamp')

    category_count = get_category_count()
    most_recent = get_most_recent_four_posts()

    # Pagination
    paginator = Paginator(post_list, 6)
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
    post = get_object_or_404(Post, id=id)

    category_count = get_category_count()
    most_recent = get_most_recent_four_posts()
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()

    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count,
        'form': form
    }

    return render(request, 'post.html', context)

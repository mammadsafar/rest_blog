from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginated_by = 2
    template_name = 'blog/post/list.html'

def postlist(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts, 'page': page})


def postdetail(request, year, month, day, post):
    post = get_object_or_404(Post, status='published', publish__year=year, publish__month=month, publish__day=day, slug=post)
    return render(request, 'blog/post/detail.html', {'post': post})

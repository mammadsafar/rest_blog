from django.shortcuts import render, reverse, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_delete.html', context={'post': post})


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

# def post_list_view(request):
#     posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/post_list.html', {'post_list': posts})
#
#
# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
#
#
# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#         else:
#             form = PostForm(request.POST, request.FILES)
#
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_create.html', context={'form': form})
#
#
# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     print(form.errors)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#
#     return render(request, 'blog/post_create.html', context={'form': form})

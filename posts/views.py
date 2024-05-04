from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post

class PostCreateView(CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'author', 'body', 'status']

class PostUpdateView(UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']

class PostDeleteView(DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('list')
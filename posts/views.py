from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Status


class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_status = Status.objects.get(name='published')
        context['post_list'] = (
            Post.objects.filter(status=published_status)
            .order_by('-created_on')
        )
        return context

class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name='draft')
        context['post_list'] = (
            Post.objects.filter(status=draft_status, author=self.request.user)
            .order_by('-created_on')
        )
        return context

class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archived = Status.objects.get(name='archived')
        context['post_list'] = (
            Post.objects.filter(status=archived, author=self.request.user)
            .order_by('-created_on')
        )
        return context

class PostDetailView(UserPassesTestMixin, DetailView):
    template_name = 'posts/detail.html'
    model = Post

    def test_func(self):
        post = self.get_object()
        if post.status.name == 'published':
            return True
        elif post.status.name == 'draft':
            return post.author == self.request.user
        elif post.status.name == 'archived':
            return self.request.user.is_authenticated
        return False

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

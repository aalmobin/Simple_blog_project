from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


class PostListView(ListView):
    """the index page view"""
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """the Detail page view"""
    model = Post
    template_name = 'blog/post_details.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    """the Create page view"""
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """the Create page view"""
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/update_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """the Create page view"""
    model = Post
    success_url = '/'
    template_name = 'blog/delete_post.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


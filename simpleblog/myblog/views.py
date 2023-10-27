from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.http import Http404


class PostListView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-createdAt']

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get(self, request, *args, **kwargs):
        try:
              return super().get(request, *args, **kwargs)
        except Http404:
              return render(request, 'error_404.html', status=404)

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields = ('title', 'title_tag', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')

def handler404(request, exception):
    return render(request, 'error_404.html', status=404)
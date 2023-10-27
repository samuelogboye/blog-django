from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.http import Http404
# from django.contrib.auth.decorators import login_required

# @login_required
# def custom_login_view(request):
#     # If a logged-in user tries to access the login view, they will be redirected to the home page
#     return redirect('home')  # Replace 'home' with the actual URL name of your home page

class PostListView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-createdAt']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    # category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts})


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
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
    # fields = ('title', 'title_tag', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = '__all__'

def handler404(request, exception):
    return render(request, 'error_404.html', status=404)
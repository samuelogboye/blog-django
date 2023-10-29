from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, SearchForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import Http404, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required

# @login_required
# def custom_login_view(request):
#     # If a logged-in user tries to access the login view, they will be redirected to the home page
#     return redirect('home')  # Replace 'home' with the actual URL name of your home page

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = Post.objects.filter(title__icontains=query)
            return render(request, 'search_results.html', {'posts': posts, 'query': query})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-createdAt']

    def get_context_data(self, *args, **kwargs):
          cat_menu = Category.objects.all()
          context = super(PostListView, self).get_context_data(*args, **kwargs)
          context["cat_menu"] = cat_menu
          return context


def category_view(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["cat_menu"] = cat_menu
        context['total_likes'] = total_likes
        return context

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

def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    # fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(AddCommentView, self).get_form_kwargs()
        kwargs['request'] = self.request  # Pass the request object to the form
        return kwargs

def category_list_view(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def handler404(request, exception):
    return render(request, 'error_404.html', status=404)
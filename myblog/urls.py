from django.urls import path
from .views import PostListView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, category_view, category_list_view, like_view, AddCommentView

urlpatterns = [
    # path("", views.home, name="home"),
    path("", PostListView.as_view(), name="home"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("article/edit/<int:pk>/", UpdatePostView.as_view(), name="update_post"),
    path("article/delete/<int:pk>/", DeletePostView.as_view(), name="delete_post"),
	path("add_category/", AddCategoryView.as_view(), name="add_category"),
	path("category/<str:cats>/", category_view, name="category"),
	path("category-list/", category_list_view, name="category-list"),
	path("like/<int:pk>/", like_view, name="like_post"),
	path("article/<int:pk>/comment/", AddCommentView.as_view(), name="add_comment"),

]
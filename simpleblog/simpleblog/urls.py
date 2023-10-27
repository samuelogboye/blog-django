from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


handler404 = 'myblog.views.handler404'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myblog.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
	# path('members/login/', LoginView.as_view(template_name='registration/login.html'), name='login'), # to ensure a current users doesn't have to login again
]

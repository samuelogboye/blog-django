from django.contrib import admin
from django.urls import path, include

handler404 = 'myblog.views.handler404'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myblog.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
]

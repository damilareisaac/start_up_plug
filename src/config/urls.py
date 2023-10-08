from django.contrib import admin
from django.urls import path, include
from app_blog import urls as app_blog_urls

# api_urls = app_blog_urls

urlpatterns = [
    path("api/v1/blog/", include(app_blog_urls)),
    # path("admin/", admin.site.urls),
]

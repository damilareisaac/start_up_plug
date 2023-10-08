from django.urls import path
from . import views

app_name = "app_blog"

POST_DETAILS = "slug/<int:year>/<int:month>/<int:day>/{}"

urlpatterns = [
    path("", views.list_posts, name="list_posts"),
    path("create/", views.create_post, name="create_post"),
    path(
        POST_DETAILS.format(""),
        views.post_detail,
        name="post_detail",
    ),
    path(
        POST_DETAILS.format("update/"),
        views.update_post,
        name="update_post",
    ),
    path(
        POST_DETAILS.format("delete/"),
        views.delete_post,
        name="delete_post",
    ),
]

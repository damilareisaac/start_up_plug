from django.shortcuts import render
from django.views.decorators import require_http_method
from app_blog.serializers import PostSerializer
from rest_framework.response import HttpResponse

# Create your views here.


@require_http_method(["POST"])
def create_post(request):
    post = PostSerializer(request.data)
    return HttpResponse(post.data)


def list_posts(request):
    ...


def post_detail(request):
    ...


def update_post(request):
    ...


def delete_post(request):
    ...

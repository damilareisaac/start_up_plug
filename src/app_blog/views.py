from django.shortcuts import render
from app_blog.models import Post

# from django.views.decorators import require_http_method
from app_blog.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


@api_view(["post"])
def create_post(request):
    s_post = PostSerializer(request.data)
    if s_post.is_valid():
        return Response(s_post.data, status.HTTP_201_CREATED)
    return Response(s_post.errors, status.HTTP_400_BAD_REQUEST)


@api_view(["get"])
def list_posts(request):
    posts = Post.objects.all()
    s_posts = PostSerializer(posts, many=True)
    return Response(s_posts.data, status.HTTP_200_OK)


def post_detail(request):
    ...


def update_post(request):
    ...


def delete_post(request):
    ...

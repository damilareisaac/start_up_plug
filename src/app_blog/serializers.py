from app_startup.serializers import TagSerializer
from models import Post

from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"

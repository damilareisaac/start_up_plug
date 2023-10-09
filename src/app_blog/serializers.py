from app_startup.serializers import TagSerializer
from .models import Post

from rest_framework.serializers import HyperlinkedModelSerializer


class PostSerializer(HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"

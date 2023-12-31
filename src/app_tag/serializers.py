from rest_framework.serializers import ModelSerializer

from app_tag.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

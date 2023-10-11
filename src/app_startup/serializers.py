from rest_framework.serializers import ModelSerializer

from app_startup.models import StartUp
from app_tag.models import Tag
from app_tag.serializers import TagSerializer


class StartUpSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = StartUp
        fields = "__all__"

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        startup = StartUp.objects.create(**validated_data)
        if tags_data:
            tags_list = [Tag.objects.get_or_create(**tag) for tag, _ in tags_data]
            startup.tags.add(tags_list)

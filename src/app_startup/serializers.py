from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, Field

from app_startup.models import StartUp, Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class StartUpSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = StartUp
        fields = "__all__"

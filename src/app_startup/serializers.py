from rest_framework.serializers import ModelSerializer

from app_startup.models import StartUp
from app_tag.serializers import TagSerializer


class StartUpSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = StartUp
        fields = "__all__"

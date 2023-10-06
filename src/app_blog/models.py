from django.db import models
from app_organizer.models import Tag, StartUp


class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    text = models.TextField()
    published_date = models.DateField()
    tags = models.ManyToManyField(
        Tag,
        related_name="posts",
    )
    start_up = models.ManyToManyField(
        StartUp,
        related_name="posts",
    )

    def __str__(self) -> str:
        return self.title

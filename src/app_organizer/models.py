from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(
        max_length=64,
        unique=True,
        help_text="A label for URL config",
    )

    def __str__(self) -> str:
        return self.name


class StartUp(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(
        max_length=64,
        unique=True,
        help_text="A label for URL config",
    )
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(
        Tag,
        related_name="start_ups",
    )

    class Meta:
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        return self.title


class NewsLink(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(
        max_length=64,
        help_text="A label for URL config",
        unique=True,
    )
    publish_date = models.DateField()
    link = models.URLField(max_length=255)
    start_up = models.ForeignKey(
        StartUp,
        on_delete=models.CASCADE,
        related_name="news_link",
    )

    def __str__(self) -> str:
        return self.title

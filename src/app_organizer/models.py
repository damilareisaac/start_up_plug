from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(
        max_length=64,
        unique=True,
        help_text="A label for URL config",
    )

    class Meta:
        ordering = ["name"]

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
        get_latest_by = "founded_date"

    def __str__(self) -> str:
        return self.name


class NewsLink(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(
        max_length=64,
        help_text="A label for URL config",
        unique=True,
    )
    published_date = models.DateField()
    link = models.URLField(max_length=255)
    start_up = models.ForeignKey(
        StartUp,
        on_delete=models.CASCADE,
        related_name="news_link",
    )

    class Meta:
        get_latest_by = "published_date"
        ordering = ["-published_date"]
        unique_together = ("slug", "start_up")
        verbose_name = "news article"

    def __str__(self) -> str:
        return f"{self.title}: {self.link}"

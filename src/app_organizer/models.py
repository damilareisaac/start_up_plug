from django.db import models
from django.utils.text import slugify

SLUG_HINT_TEXT = "A label for URL config"


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(
        max_length=64,
        unique=True,
        help_text=SLUG_HINT_TEXT,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class StartUp(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(
        max_length=64,
        unique=True,
        help_text=SLUG_HINT_TEXT,
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

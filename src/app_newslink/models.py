from django.db import models

from app_organizer.models import StartUp


# Create your models here.
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

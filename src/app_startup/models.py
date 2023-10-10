from django.db import models
from django.utils.text import slugify

from app_tag.models import Tag

SLUG_HINT_TEXT = "A label for URL config"


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
        ordering = ("-founded_date",)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

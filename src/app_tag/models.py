from django.db import models
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField

SLUG_HINT_TEXT = "A label for URL config"


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = AutoSlugField(
        populate_from="name",
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

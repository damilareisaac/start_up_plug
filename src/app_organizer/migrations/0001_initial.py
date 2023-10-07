# Generated by Django 4.2.6 on 2023-10-06 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                (
                    "slug",
                    models.SlugField(
                        help_text="A label for URL config", max_length=64, unique=True
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="StartUp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "slug",
                    models.SlugField(
                        help_text="A label for URL config", max_length=64, unique=True
                    ),
                ),
                ("description", models.TextField()),
                ("founded_date", models.DateField()),
                ("contact", models.EmailField(max_length=254)),
                ("website", models.URLField(max_length=255)),
                (
                    "tags",
                    models.ManyToManyField(
                        related_name="start_ups", to="app_organizer.tag"
                    ),
                ),
            ],
            options={
                "ordering": ["-founded_date"],
            },
        ),
        migrations.CreateModel(
            name="NewsLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64)),
                (
                    "slug",
                    models.SlugField(
                        help_text="A label for URL config", max_length=64, unique=True
                    ),
                ),
                ("published_date", models.DateField()),
                ("link", models.URLField(max_length=255)),
                (
                    "start_up",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="news_link",
                        to="app_organizer.startup",
                    ),
                ),
            ],
            options={
                "verbose_name": "news article",
                "ordering": ["-published_date"],
                "get_latest_by": "published_date",
            },
        ),
        migrations.AddIndex(
            model_name="startup",
            index=models.Index(fields=["name"], name="app_organiz_name_4875eb_idx"),
        ),
        migrations.AlterUniqueTogether(
            name="newslink",
            unique_together={("slug", "start_up")},
        ),
    ]

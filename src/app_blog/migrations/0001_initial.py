# Generated by Django 4.2.6 on 2023-10-10 22:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_startup", "0001_initial"),
        ("app_tag", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("slug", models.CharField(max_length=64)),
                ("text", models.TextField()),
                ("published_date", models.DateField()),
                (
                    "start_up",
                    models.ManyToManyField(
                        related_name="posts", to="app_startup.startup"
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(related_name="posts", to="app_tag.tag"),
                ),
            ],
            options={
                "verbose_name": "blog post",
                "ordering": ["-published_date", "title"],
                "get_latest_by": "published_date",
            },
        ),
    ]

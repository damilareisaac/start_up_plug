from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ("app_startup", "0001_initial"),
    ]
    operations = [
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
                        on_delete=models.deletion.CASCADE,
                        related_name="news_link",
                        to="app_startup.startup",
                    ),
                ),
            ],
            options={
                "verbose_name": "news article",
                "ordering": ["-published_date"],
                "get_latest_by": "published_date",
            },
        ),
        migrations.AlterUniqueTogether(
            name="newslink",
            unique_together={("slug", "start_up")},
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-10 22:52

from django.db import migrations, models


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
    ]
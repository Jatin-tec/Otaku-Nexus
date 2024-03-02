# Generated by Django 5.0.2 on 2024-03-02 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnimeType",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Anime",
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
                ("title", models.CharField(max_length=100)),
                ("synopsis", models.TextField()),
                ("mal_id", models.IntegerField(unique=True)),
                ("episode_count", models.IntegerField()),
                (
                    "image",
                    models.ImageField(
                        default="anime_pictures/default.jpg", upload_to="anime_pictures"
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="anime.animetype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Episodes",
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
                ("title", models.CharField(max_length=100)),
                ("synopsis", models.TextField()),
                ("episode_number", models.IntegerField()),
                ("duration", models.IntegerField()),
                ("aired", models.DateTimeField()),
                ("filler", models.BooleanField()),
                ("recap", models.BooleanField()),
                ("mal_url", models.URLField()),
                (
                    "anime",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="anime.anime"
                    ),
                ),
            ],
        ),
    ]

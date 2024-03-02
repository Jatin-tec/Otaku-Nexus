# Generated by Django 5.0.2 on 2024-03-02 18:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0003_animetype_anime_episodes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="anime",
            name="type",
        ),
        migrations.RemoveField(
            model_name="episodes",
            name="anime",
        ),
        migrations.AddField(
            model_name="profile",
            name="about_me",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name="AnimeType",
        ),
        migrations.DeleteModel(
            name="Anime",
        ),
        migrations.DeleteModel(
            name="Episodes",
        ),
    ]

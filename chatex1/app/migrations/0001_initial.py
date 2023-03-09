# Generated by Django 4.1.5 on 2023-03-09 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Channel",
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
                ("name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("name", models.TextField()),
                (
                    "channels",
                    models.ManyToManyField(
                        related_name="channel_users",
                        related_query_name="channel_user",
                        to="app.channel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("text", models.TextField()),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.channel"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="channel",
            name="users",
            field=models.ManyToManyField(to="app.user"),
        ),
    ]

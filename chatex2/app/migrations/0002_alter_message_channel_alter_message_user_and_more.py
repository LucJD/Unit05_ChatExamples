# Generated by Django 4.1.5 on 2023-03-09 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="channel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages_on_channel",
                to="app.channel",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages_from_user",
                to="app.user",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="channels",
            field=models.ManyToManyField(
                related_name="channel_users", to="app.channel"
            ),
        ),
    ]

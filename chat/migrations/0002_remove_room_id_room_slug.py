# Generated by Django 4.2.3 on 2023-07-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="id",
        ),
        migrations.AddField(
            model_name="room",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=120, primary_key=True, serialize=False
            ),
        ),
    ]

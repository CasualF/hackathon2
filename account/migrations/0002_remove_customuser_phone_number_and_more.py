# Generated by Django 4.2.3 on 2023-07-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="phone_number",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
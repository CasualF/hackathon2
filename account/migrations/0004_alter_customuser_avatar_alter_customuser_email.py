# Generated by Django 4.2.3 on 2023-07-22 05:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_alter_customuser_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatars"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
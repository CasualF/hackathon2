# Generated by Django 4.2.3 on 2023-07-23 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0016_alter_contact_contact2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="contact2",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contact",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

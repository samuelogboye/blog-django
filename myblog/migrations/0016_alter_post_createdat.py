# Generated by Django 4.2.6 on 2023-10-29 00:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("myblog", "0015_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="createdAt",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myblog", "0002_post_createdat_post_updatedat"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title_tag",
            field=models.CharField(default="My Awesome Blog", max_length=200),
        ),
    ]

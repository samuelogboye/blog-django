# Generated by Django 4.2.6 on 2023-10-28 21:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myblog", "0012_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(editable=False, max_length=255),
        ),
    ]
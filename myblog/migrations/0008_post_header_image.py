# Generated by Django 4.2.6 on 2023-10-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myblog", "0007_alter_post_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="header_image",
            field=models.FileField(blank=True, null=True, upload_to="images/"),
        ),
    ]
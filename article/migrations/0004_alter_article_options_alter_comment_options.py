# Generated by Django 5.1.4 on 2025-01-07 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0003_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"ordering": ["-created_date"]},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-comment_date"]},
        ),
    ]

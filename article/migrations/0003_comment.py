# Generated by Django 5.1.4 on 2025-01-07 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0002_article_article_image_alter_article_author_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "comment_author",
                    models.CharField(max_length=50, verbose_name="Yazar"),
                ),
                (
                    "comment_content",
                    models.TextField(max_length=200, verbose_name="Yorum"),
                ),
                (
                    "comment_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="article.article",
                        verbose_name="Makale",
                    ),
                ),
            ],
        ),
    ]

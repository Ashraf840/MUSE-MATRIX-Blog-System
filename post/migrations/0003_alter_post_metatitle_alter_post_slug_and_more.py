# Generated by Django 5.0.2 on 2024-03-16 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_latestpost_mostpopularpost_relatedpost_trendingpost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="metaTitle",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]

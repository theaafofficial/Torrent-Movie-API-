# Generated by Django 4.1 on 2022-08-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rest_api", "0002_rename_rotten_tomatoes_movies_rotten_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movies",
            name="imdb_rating",
            field=models.FloatField(default=None),
        ),
    ]

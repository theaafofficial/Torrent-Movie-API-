# Generated by Django 4.1 on 2022-08-26 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rest_api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movies", old_name="rotten_tomatoes", new_name="rotten_rating",
        ),
    ]

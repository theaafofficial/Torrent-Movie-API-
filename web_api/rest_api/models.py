from dataclasses import fields
from django.contrib.postgres.fields import ArrayField
from django.db import models
from jsonfield import JSONField

# Create your models here.
class Movies(models.Model):
    name = models.TextField( db_index=True, default=None)
    year = models.IntegerField(default=None)
    genre = models.TextField(null=True)
    plot = models.TextField(null=True)
    imdb_rating = models.FloatField(default=None,null=True)
    rotten_rating = models.IntegerField(default=None,null=True)
    torrent_720p = models.TextField(null=True)
    torrent_1080p = models.TextField(null=True)
    subtitles = models.TextField(null=True)
    images = ArrayField(models.TextField(null=True))
    cast = ArrayField(models.TextField(null=True))
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'year'],
                name="movies_pkey"
            )
        ]
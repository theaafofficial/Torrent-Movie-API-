from rest_framework import serializers
from .models import Movies
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ["name", "plot", "year", "genre", "imdb_rating","rotten_rating", "torrent_720p","torrent_1080p","subtitles","images","cast"]
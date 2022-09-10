from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movies
from .serializers import MovieSerializer


class MoviesApi(APIView):

    def get(self, request, *args, **kwargs):

        movies = Movies.objects.all()
        seriliazers = MovieSerializer(movies, many=True)
        return Response(seriliazers.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'plot': request.data.get('plot'),
            'year': request.data.get('year'),
            'genre': request.data.get('genre'),
            'imdb_rating': request.data.get('imdb_rating'),
            'rotten_rating': request.data.get('rotten_rating'),
            'torrent_720p': request.data.get('torrent_720p'),
            'torrent_1080p': request.data.get('torrent_1080p'),
            'subtitles': request.data.get('subtitles'),
            'images': request.data.get('images'),
            'cast': request.data.get('cast'),

        }

        serializer = MovieSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieByName(APIView):

    def get(self, request, movie_name, *args, **kwargs):
        movies = Movies.objects.filter(name__icontains=movie_name)
        if not movies:
            return Response({"response": f"No movie found by {movie_name}"}, status=status.HTTP_404_NOT_FOUND)
        seriliazer = MovieSerializer(movies,many=True)
        return Response(seriliazer.data, status=status.HTTP_200_OK)

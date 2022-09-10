from django.urls import path
from django.urls import path, include
from .views import (
    MoviesApi,
    MovieByName
)

urlpatterns = [
    path('movies', MoviesApi.as_view()),
    path('movies/<str:movie_name>', MovieByName.as_view()),
   
]

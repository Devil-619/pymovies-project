from django.urls import path
from .views import MovieListView, GenreMovieListView, MovieSearchResult, WatchListView, RecommendListView
from . import views

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-home'),
    path('genre/<str:genre>/', GenreMovieListView.as_view(), name='movie-genre'),
    path('movie/<str:title>/', views.MovieDetail, name='movie-detail'),
    path('watchlist/<str:username>/', WatchListView.as_view(), name='user-watchlist'),
    path('recommendations/<str:username>/', RecommendListView.as_view(), name='user-recommend'),
    path('search/', views.MovieSearch, name='movie-search'),
    path('search-results/<str:title>/', MovieSearchResult.as_view(), name='movie-search-result'),
    path('about/', views.about, name='movie-about'),
]

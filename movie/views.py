import recommend
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from users.models import Profile, ThroughModel
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'movie/home.html'
    context_object_name = 'movies'
    ordering = ['-rating']
    paginate_by = 6

class GenreMovieListView(ListView):
    model = Movie
    template_name = 'movie/genre.html'
    context_object_name = 'movies'
    paginate_by = 6

    def get_queryset(self):
        movie = self.kwargs.get('genre')
        return Movie.objects.filter(genre=movie).order_by('-rating')

class WatchListView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'movie/watchlist.html'
    context_object_name = 'movies'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        profile = Profile.objects.get(user=user)
        return profile.watchlist.all().order_by('-rating')

class RecommendListView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'movie/recommend_list.html'
    context_object_name = 'movies'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        profile = Profile.objects.get(user=user)
        history_model = ThroughModel.objects.filter(profile=profile).order_by('-date_viewed')
        recommend_list = []
        for obj in history_model:
            title = obj.movie.title
            temp_list = recommend.recommend(title)
            recommend_list.extend(temp_list)
        recommend_list = recommend.remove_duplicates(recommend_list)
        return Movie.objects.filter(title__in=recommend_list).order_by('-rating')

def MovieDetail(response, **kwargs):
    title = kwargs.get('title')
    present = "FALSE"
    if response.user.is_authenticated:
        profile = Profile.objects.get(user = response.user)
        movie = Movie.objects.get(title = title)
        history_model = ThroughModel.objects.filter(profile=profile).order_by('date_viewed')
        ThroughModel.objects.create(profile=profile, movie=movie)
        if history_model.count() > 5:
            history_model.first().delete()
        watchlist = profile.watchlist.filter(title = title)
        if watchlist.count() == 0:
            present = 'FALSE'
        else:
            present = 'TRUE'
        if response.method == 'POST':
            if response.POST.get("save") == "add":
                profile.watchlist.add(movie)
                present = "TRUE"
            elif response.POST.get("save") == "remove":
                profile.watchlist.remove(movie)
                present = "FALSE"
            else:
                pass
    movies = recommend.recommend(title)
    movies = Movie.objects.filter(title__in = movies).order_by('-rating')
    current = Movie.objects.filter(title = title).first()
    context = {
        'movies' : movies,
        'current' : current,
        'present' : present
    }
    return render(response, 'movie/detail.html', context)

def MovieSearch(response):
    if response.POST.get("search"):
        title = response.POST.get("searchField")
        return redirect('movie-search-result', title)
        # movies = Movie.objects.filter(title__contains = title).order_by('title')
        # context = {
        #     'movies' : movies
        # }
        # if movies.count() == 0:
        #     messages.error(request, f'Movie not found')
    return render(response, 'movie/search_movie.html')

class MovieSearchResult(ListView):
    model = Movie
    template_name = 'movie/search_result.html'
    context_object_name = 'movies'
    paginate_by = 6

    def get_queryset(self):
        title = self.kwargs.get('title')
        movies = Movie.objects.filter(title__contains = title).order_by('title')
        return movies

def about(request):
    return render(request, 'movie/about.html', {'title' : 'About'})
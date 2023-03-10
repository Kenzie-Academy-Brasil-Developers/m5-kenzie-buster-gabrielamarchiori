from django.urls import path
from .views import MovieView, MovieDetailView
from . import views

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:movie_id>/', views.MovieDetailView.as_view()),
    path('movies/<int:movie_id>/orders/', views.MovieOrderView.as_view())
]

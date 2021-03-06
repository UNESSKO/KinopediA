from django.urls import path

from . import views

urlpatterns = [
    path("", views.MovieView.as_view()),
    path("category/", views.CategoryView.as_view(), name="category"),
    path("filter/", views.FilterMoviesView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path("add-rating/", views.AddRating.as_view(), name="add_rating"),
    path("json-filter/", views.JsonFilterMoviesView.as_view(), name="json_filter"),
    path("<slug:slug>/", views.MovieDetalView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("persone/<str:slug>/", views.PersoneView.as_view(), name="persone_detail"),
]
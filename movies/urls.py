from django.urls import path
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView, MovieStatsView



urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
    path('movies/stats/', MovieStatsView.as_view(), name='movie-stats-view'),
]

from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
]

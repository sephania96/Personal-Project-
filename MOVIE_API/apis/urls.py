from django.urls import path

from .views import ListMovie, DetailMovie

urlpatterns = [
    path("", ListMovie.as_view()),
    path("<int:pk>/", DetailMovie.as_view()),
]
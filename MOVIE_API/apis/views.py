from django.shortcuts import render
from rest_framework import generics
from movies import models
from .serializers import moviesSerializer
# Create your views here.

class ListMovie(generics.ListCreateAPIView):
    queryset = models.movies.objects.all()
    serializer_class = moviesSerializer

class DetailMovie(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.movies.objects.all()
    serializer_class = moviesSerializer
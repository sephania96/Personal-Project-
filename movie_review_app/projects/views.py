from django.shortcuts import render
from .models import project
# Create your views here.

def project_index(request):
    projects = project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    movie_detail = project.objects.get(pk=pk)
    context = {
        "project": movie_detail
    }
    return render(request, "projects/project_detail.html", context)
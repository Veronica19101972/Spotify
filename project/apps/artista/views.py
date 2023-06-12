from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import context

from . import models

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "artista/index.html")

def artista_list(request):
    artistas = models.Artista.objects.all()
    context = {"artistas": artistas}
    return render(request, "artista/artista_list.html", context)
    
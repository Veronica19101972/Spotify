from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import context

from . import models
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "album/index.html")


def album_list(request):
    albumes = models.Album.objects.all()
    context = {"albumes": albumes}
    return render(request, "album/album_list.html", context)

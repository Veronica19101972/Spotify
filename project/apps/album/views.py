from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import context

from . import models, forms


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "album/index.html")

def album_list(request):
    albumes = models.Album.objects.all()
    context = {"albumes": albumes}
    return render(request, "album/album_list.html", context)

def album_create(request):
    if request.method == "POST":
        form = forms.albumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("album:index")
    else:
        form = forms.albumForm()
    return render(request, "album/album_create.html", {"form": form})


        
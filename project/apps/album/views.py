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

def album_delete(request, id):
    album = models.Album.objects.get(id=id)
    if request.method == "POST":
        album.delete()
        return redirect("album:index")
    return render(request, "album/album_delete.html", {"album": album})

def album_update(request, id):
    album = models.Album.objects.get(id=id)
    if request.method == "POST":
        form = forms.albumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("album:index")
    else:
        form = forms.albumForm(instance=album)
    return render(request, "album/album_update.html", {"form": form})


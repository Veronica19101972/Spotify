from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import context

from . import models, forms

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "artista/index.html")

def artista_list(request):
    artistas = models.Artista.objects.all()
    context = {"artistas": artistas}
    return render(request, "artista/artista_list.html", context)
    
def artista_create(request):
    if request.method == "POST":
        form = forms.artistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("artista:index")
    else:
        form = forms.artistaForm()
    return render(request, "artista/artista_create.html", {"form": form})

def artista_delete(request, id):
    artista = models.Artista.objects.get(id=id)
    if request.method == "POST":
        artista.delete()
        return redirect("artista:index")
    return render(request, "artista/artista_delete.html", {"artista": artista})

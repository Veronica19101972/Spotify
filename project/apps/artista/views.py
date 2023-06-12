from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import context

from . import models, forms
from django.urls import reverse_lazy

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "artista/index.html")

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ArtistaList(ListView):
    model = models.Artista
    template_name = "artista/artista_list.html"
    context_object_name = "artistas"
    
class ArtistaCreate(CreateView):
    model = models.Artista
    form_class = forms.ArtistaForm
    template_name = "artista/artista_create.html"
    success_url = reverse_lazy("artista:index")    

class ArtistaDelete(DeleteView):
    model = models.Artista
    template_name = "artista/artista_delete.html"
    success_url = reverse_lazy("artista:index")    
    
class ArtistaUpdate(UpdateView):
    model = models.Artista
    form_class = forms.ArtistaForm
    template_name = "artista/artista_update.html"
    success_url = reverse_lazy("artista:index")    


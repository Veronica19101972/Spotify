
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from . import models, forms
from django.urls import reverse_lazy

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "album/index.html")

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class AlbumList(ListView):
    model = models.Album
    template_name = "album/album_list.html"
    context_object_name = "albumes"
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Album.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Album.objects.all()
        return object_list
       
class AlbumCreate(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    #template_name = "album/album_create.html"
    success_url = reverse_lazy("album:index")    

class AlbumDelete(DeleteView):
    model = models.Album
    #template_name = "album/album_delete.html"
    success_url = reverse_lazy("album:album_list")
    
class AlbumUpdate(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    #template_name = "album/album_update.html"
    success_url = reverse_lazy("album:album_list")
    
class AlbumDetail(DetailView):
    model = models.Album
    
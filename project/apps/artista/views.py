
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms
from django.urls import reverse_lazy

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "artista/index.html")

from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ArtistaList(ListView):
    model = models.Artista
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Artista.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Artista.objects.all()
        return object_list
    
class ArtistaCreate(LoginRequiredMixin, CreateView):
    model = models.Artista
    form_class = forms.ArtistaForm
    success_url = reverse_lazy("artista:index")    

class ArtistaDelete(DeleteView):
    model = models.Artista
    success_url = reverse_lazy("artista:artista_list")    
    
class ArtistaUpdate(UpdateView):
    model = models.Artista
    form_class = forms.ArtistaForm
    success_url = reverse_lazy("artista:artista_list")    

class ArtistaDetail(DetailView):
    model = models.Artista
    
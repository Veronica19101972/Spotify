
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms
from django.urls import reverse_lazy

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "cuenta/index.html")

    
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CuentaList(ListView):
    model = models.Cuenta
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Cuenta.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Cuenta.objects.all()
        return object_list
    
class CuentaCreate(LoginRequiredMixin, CreateView):
    model = models.Cuenta
    form_class = forms.cuentaForm
    success_url = reverse_lazy("cuenta:index")    

class CuentaDelete(DeleteView):
    model = models.Cuenta
    success_url = reverse_lazy("cuenta:cuenta_list")    
    
class CuentaUpdate(UpdateView):
    model = models.Cuenta
    form_class = forms.cuentaForm
    success_url = reverse_lazy("cuenta:cuenta_list")    

class CuentaDetail(DetailView):
    model = models.Cuenta

    
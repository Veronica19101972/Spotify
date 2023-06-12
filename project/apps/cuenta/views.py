from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import context

from . import models, forms
from django.urls import reverse_lazy

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "cuenta/index.html")

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CuentaList(ListView):
    model = models.Cuenta
    template_name = "cuenta/cuenta_list.html"
    context_object_name = "cuentas"
    
class CuentaCreate(CreateView):
    model = models.Cuenta
    form_class = forms.cuentaForm
    template_name = "cuenta/cuenta_create.html"
    success_url = reverse_lazy("cuenta:index")    

class CuentaDelete(DeleteView):
    model = models.Cuenta
    template_name = "cuenta/cuenta_delete.html"
    success_url = reverse_lazy("cuenta:index")    
    
class CuentaUpdate(UpdateView):
    model = models.Cuenta
    form_class = forms.cuentaForm
    template_name = "cuenta/cuenta_update.html"
    success_url = reverse_lazy("cuenta:index")

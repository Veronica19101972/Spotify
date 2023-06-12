from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import context

from . import models, forms

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "cuenta/index.html")

def cuenta_list(request):
    cuentas = models.Cuenta.objects.all()
    context = {"cuentas": cuentas}
    return render(request, "cuenta/cuenta_list.html", context)
    
def cuenta_create(request):
    if request.method == "POST":
        form = forms.cuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cuenta:index")
    else:
        form = forms.cuentaForm()
    return render(request, "cuenta/cuenta_create.html", {"form": form})
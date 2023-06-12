from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import context

from . import models

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "cuenta/index.html")

def cuenta_list(request):
    cuentas = models.Cuenta.objects.all()
    context = {"cuentas": cuentas}
    return render(request, "cuenta/cuenta_list.html", context)
    
from django.contrib import admin

# Register your models here.
from . import models

#admin.site.register(models.Artista)

@admin.register(models.Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display=("apellido", "nombre", "nacionalidad")
    search_fields = ("apellido", "nombre",)
    list_filter = ("apellido", "nombre",)
    ordering = ("apellido", "nombre",)
    
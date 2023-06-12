from django.contrib import admin

# Register your models here.
from . import models

#admin.site.register(models.Cuenta)

@admin.register(models.Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display=("apellido", "nombre", "dni", "nacionalidad", "fecha_de_alta")
    search_fields = ("apellido", "nombre", "dni",)
    list_filter = ("apellido", "nombre", "dni",)
    ordering = ("apellido", "nombre", "dni",)
    

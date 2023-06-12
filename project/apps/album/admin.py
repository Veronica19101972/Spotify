from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = " Albumes "
admin.site.site_header = " Aplicación de Spotify "

#admin.site.register(models.Album)

@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=("nombre", "fecha_de_lanzamiento", "estilo")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
    
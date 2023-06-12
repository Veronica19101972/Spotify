from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("cuenta/", include(("cuenta.urls", "cuenta"))),
    path("artista/", include(("artista.urls", "artista"))),
    path("album/", include(("album.urls", "album"))),
]

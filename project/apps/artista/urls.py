from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("artista_list/", views.artista_list, name="artista_list"),
     path("artista_create/", views.artista_create, name="artista_create"),
]

urlpatterns += staticfiles_urlpatterns()

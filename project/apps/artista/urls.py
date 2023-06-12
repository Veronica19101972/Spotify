from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("artista_list/", views.artista_list, name="artista_list"),
     path("artista_create/", views.artista_create, name="artista_create"),
     path("artista_delete/<int:id>", views.artista_delete, name="artista_delete"),
     path("artista_update/<int:id>", views.artista_update, name="artista_update"),

]

urlpatterns += staticfiles_urlpatterns()

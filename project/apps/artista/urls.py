from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("artista_list/", views.artista_list, name="artista_list"),
]

urlpatterns += staticfiles_urlpatterns()

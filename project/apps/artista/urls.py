from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [    
     path("", views.index, name="index"),
     path("artista_list/", views.ArtistaList.as_view(), name="artista_list"),
     path("artista_create/", views.ArtistaCreate.as_view(), name="artista_create"),
     path("artista_delete/<int:pk>", views.ArtistaDelete.as_view(), name="artista_delete"),
     path("artista_update/<int:pk>", views.ArtistaUpdate.as_view(), name="artista_update"),
]

urlpatterns += staticfiles_urlpatterns()

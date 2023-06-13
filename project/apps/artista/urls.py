
from django.urls import path

from . import views

urlpatterns = [    
     path("", views.index, name="index"),
     path("artista/list/", views.ArtistaList.as_view(), name="artista_list"),
     path("artista/create/", views.ArtistaCreate.as_view(), name="artista_create"),
     path("artista/delete/<int:pk>", views.ArtistaDelete.as_view(), name="artista_delete"),
     path("artista/update/<int:pk>", views.ArtistaUpdate.as_view(), name="artista_update"),
     path("artista/detail/<int:pk>", views.ArtistaDetail.as_view(), name="artista_detail"),
]


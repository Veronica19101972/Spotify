from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("album_list/", views.AlbumList.as_view(), name="album_list"),
     path("album_create/", views.AlbumCreate.as_view(), name="album_create"),
     path("album_delete/<int:pk>", views.AlbumDelete.as_view(), name="album_delete"),
     path("album_update/<int:pk>", views.AlbumUpdate.as_view(), name="album_update"),
]

urlpatterns += staticfiles_urlpatterns()

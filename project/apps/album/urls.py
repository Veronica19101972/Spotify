#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("album/list/", views.AlbumList.as_view(), name="album_list"),
     path("album/create/", views.AlbumCreate.as_view(), name="album_create"),
     path("album/delete/<int:pk>", views.AlbumDelete.as_view(), name="album_delete"),
     path("album/update/<int:pk>", views.AlbumUpdate.as_view(), name="album_update"),
     path("album/detail/<int:pk>", views.AlbumDetail.as_view(), name="album_detail"),

]

#urlpatterns += staticfiles_urlpatterns()

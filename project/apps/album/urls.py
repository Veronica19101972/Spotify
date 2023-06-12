from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("album_list/", views.album_list, name="album_list"),
     path("album_create/", views.album_create, name="album_create"),

]

urlpatterns += staticfiles_urlpatterns()

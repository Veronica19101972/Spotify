from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("cuenta_list/", views.cuenta_list, name="cuenta_list"),
     path("cuenta_create/", views.cuenta_create, name="cuenta_create"),
     path("cuenta_delete/<int:id>", views.cuenta_delete, name="cuenta_delete"),

]

urlpatterns += staticfiles_urlpatterns()

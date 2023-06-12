from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("cuenta_list/", views.cuenta_list, name="cuenta_list"),
]

urlpatterns += staticfiles_urlpatterns()

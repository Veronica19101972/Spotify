from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("cuenta_list/", views.CuentaList.as_view(), name="cuenta_list"),
     path("cuenta_create/", views.CuentaCreate.as_view(), name="cuenta_create"),
     path("cuenta_delete/<int:pk>", views.CuentaDelete.as_view(), name="cuenta_delete"),
     path("cuenta_update/<int:pk>", views.CuentaUpdate.as_view(), name="cuenta_update"),
]

urlpatterns += staticfiles_urlpatterns()

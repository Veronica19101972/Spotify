
from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("cuenta/list/", views.CuentaList.as_view(), name="cuenta_list"),
     path("cuenta/create/", views.CuentaCreate.as_view(), name="cuenta_create"),
     path("cuenta/delete/<int:pk>", views.CuentaDelete.as_view(), name="cuenta_delete"),
     path("cuenta/update/<int:pk>", views.CuentaUpdate.as_view(), name="cuenta_update"),
     path("cuenta/detail/<int:pk>", views.CuentaDetail.as_view(), name="cuenta_detail"),
     
]

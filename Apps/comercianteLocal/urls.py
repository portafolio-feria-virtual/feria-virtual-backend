from .views import *
from django.urls import path, include

urlpatterns =[
    path('createSolicitudCompra/', CrearSolicitudCompraView.as_view())
]
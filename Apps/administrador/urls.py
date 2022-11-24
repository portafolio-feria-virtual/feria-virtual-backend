from .views import *
from django.urls import path,include

urlpatterns = [
    path('addContract/', CrearContratoView.as_view()),
    path('viewContract/', VerContratosView.as_view()),
    path('buscarContrato/', BuscarContratoView.as_view()),
]

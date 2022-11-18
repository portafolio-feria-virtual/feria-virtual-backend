from .views import *
from django.urls import path,include

urlpatterns = [
    path('addContract/', CrearContratoView.as_view()),
    path('viewContract/', VerContratoView.as_view()),
    path('viewStatusProcess', VerProcesoVentasView.as_view())
]

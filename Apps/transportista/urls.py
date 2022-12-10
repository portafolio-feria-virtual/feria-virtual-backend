from .views import *
from django.urls import path, include


urlpatterns = [
    path('createOfferTransport/', addPostulacionLicitacionView.as_view()),
    path("seeAllPostulaciones/", seeAllPostulaciones.as_view()),
    path("acceptBid/",AceptarRechazarPostulacionTransporteView.as_view()),
    path("packageTracking",EstadoEnvioGeneralView.as_view()),
    path("changeTracking",cambiarEstadoEnvioView.as_view()),
]

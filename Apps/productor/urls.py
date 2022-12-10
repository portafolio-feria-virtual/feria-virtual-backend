from .views import *
from django.urls import path, include
from rest_framework import routers
router  = routers.DefaultRouter()
# router.register(r'createSale', VentaLocalViewSet)


urlpatterns = [
     path('createOffer/', OfertaView.as_view()),
     path('createSale/', VentaLocalCreateView.as_view()),
     path('uploadImage/', ImagenVentaLocalView.as_view()),
     path("seeAllOffer/",SeeAllOfferView.as_view()),
     path("acceptBid/", AceptarRechazarAdjudicacionView.as_view()),
     path("packageTrackingGeneral/",EstadoEnvioGeneralView.as_view()),
     path("packageTrackingProducer/", EstadoEnvioProductorView.as_view()),
     path("confirmPreparation/",MarcarEnvio.as_view())
     #path("retrieveImages/", RetrieveImagesView.as_view()),

   

]
from .views import *
from django.urls import path, include


urlpatterns = [
    path('createOfferTransport/', addPostulacionLicitacionView.as_view()),
    path("seeAllPostulations/", SeeAllPostulations.as_view()),
    path("acceptBid/",AcceptDeclineTransportPostulationView.as_view()),
    path("packageTracking/",ShippingStatusGeneralView.as_view()),
    path("changeTracking/",UpdateShippingStatusView.as_view()),
    path("seeAllBidsAvailable/",ListAllBidsAvailablesView.as_view()),
]

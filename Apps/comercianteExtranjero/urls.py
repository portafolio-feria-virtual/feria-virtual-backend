from .views import *
from django.urls import path, include

urlpatterns=[
    path('createBid/', AddBidView.as_view()),
    path('searchBid/', SearchBidView.as_view()),
    path('listBid/', ListBidView.as_view()),
    path('listOffersProducer/', ListOffersProductorView.as_view()),
    path('listCarriersPostulation/', ListCarriersPostulationView.as_view()),
    path('editBid/',UpdateBid.as_view()),
    path('extendCloseDateBid/',EditCloseDateView.as_view()),
    path('acceptProducerOffer/',AcceptDeclineOfferProducerView.as_view()),
    path('acceptCarriersPostulation/',AcceptDeclineTransportPostulationView.as_view()),
    path('shippingStatusBid/',ShippingStatusBidView.as_view()),
    #path('seeLicitacionOfertasUser/', SeeAllLicitacionWithOfferView.as_view()),
]
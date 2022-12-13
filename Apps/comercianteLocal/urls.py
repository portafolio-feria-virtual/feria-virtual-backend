from .views import *
from django.urls import path, include

urlpatterns =[
    path('createBuyingOffer/', CreateBuyingOfferView.as_view()),
    path('seeAllSalesAvailable/', ListAllSalesAvailablesView.as_view()),
    path('seeAllBuyOffers/', ListAllBuyOffersView.as_view()),

]
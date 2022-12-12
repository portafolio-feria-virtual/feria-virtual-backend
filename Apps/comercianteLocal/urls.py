from .views import *
from django.urls import path, include

urlpatterns =[
    path('createBuyingOffer/', CreateBuyingOfferView.as_view())
]
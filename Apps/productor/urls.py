from .views import *
from django.urls import path, include

urlpatterns = [
    path('createOffer/', OfertaView.as_view())

]
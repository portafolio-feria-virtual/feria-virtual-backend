from .views import *
from django.urls import path, include


urlpatterns = [
    path('createOfferTransport/', addPostulacionLicitacionView.as_view()),
]

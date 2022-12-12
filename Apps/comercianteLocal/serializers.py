from dataclasses import fields
from rest_framework import serializers
from .models import *

class BuyingOfferSerializer(serializers.Serializer): 
    class Meta:
        model = BuyingOffer
        fields = ('producer', 'localTrader', 'status', 'orderDate', 'transport')
        
from rest_framework import serializers
from .models import *
class addTransportPostulationSerializer (serializers.ModelSerializer):
    class Meta:
        model = TransportPostulation
        fields = ("__all__")


class ShippingSerializer (serializers.ModelSerializer):

    class Meta:
        model =Shipping 
        fields = ("__all__")
from dataclasses import fields
from rest_framework import serializers
from .models import *

class SolicitudCompraSerializer(serializers.Serializer): 
    class Meta:
        model = SolicitudCompra
        fields = ('productor', 'localClient', 'status', 'orderDate', 'transport')
        
from dataclasses import fields
from rest_framework import serializers
from .models import *


class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = ('name', 'description', 'productorDescription', 'offer', 'unitPrice','adminArchives', 'techArchives', 'economicArchives')

    def validate_unitPrice (self, value):
        if value >0:
            return value
        else: 
            raise serializers.ValidationError('Precio unitario debe ser mayor a 0')
 

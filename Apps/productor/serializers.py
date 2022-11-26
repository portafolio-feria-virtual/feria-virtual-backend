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


class VentaLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaLocal
        fields= '__all__'

    def create(self, validated_data):
        images = self.context["images"]
        ventaLocal = VentaLocal.objects.create(**validated_data)
        for image in images:
            ImagenVentaLocal.objects.create(ventaLocal=ventaLocal, image=image )

        return ventaLocal

    

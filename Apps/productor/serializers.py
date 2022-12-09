from dataclasses import fields
from rest_framework import serializers
from .models import *


class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'

    def validate_unitPrice (self, value):
        if value >0:
            return value
        else: 
            raise serializers.ValidationError('Precio unitario debe ser mayor a 0')


class VentaLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaLocal
        fields= '__all__'

    # def create(self, validated_data):
    #     images = self.context["images"]
    #     ventaLocal = VentaLocal.objects.create(**validated_data)
    #     for image in images:
    #         ImagenVentaLocal.objects.create(ventaLocal=ventaLocal, image=image )

    #     return ventaLocal


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagenVentaLocal
        fields = '__all__'

    
# class OfertaWithPostulacionTransporteSerializer(serializers.ModelSerializer):
#     postulacionlicitaciontransporte_set = serializers.StringRelatedField(many=True)
    
#     class Meta:
#         model= Licitacion
#         fields= ("__all__")
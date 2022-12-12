from dataclasses import fields
from rest_framework import serializers
from .models import *


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def validate_unitPrice (self, value):
        if value >0:
            return value
        else: 
            raise serializers.ValidationError('Unit price must be greater than 0')


class LocalSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalSale
        fields= '__all__'

class LocalSaleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocalSaleImage
        fields = '__all__'


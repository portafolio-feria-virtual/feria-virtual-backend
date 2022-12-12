from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import *
from datetime import datetime
from django.utils import timezone
from Apps.productor.serializers import OfferSerializer
from Apps.transportista.serializers import addTransportPostulationSerializer

# It creates a serializer for the UserAccount model.
class BidSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Bid
        fields = ('name','description','country','region','city','street','postalCode','productList','maxAmount','processStatus','initDate','closeDate','extranjero')
    
    nowDate = datetime.now().date()
    
    def validate_closeDate(self,value):
        if(self.nowDate > value):
            raise serializers.ValidationError('Close Date is prior to current date')
        return value
    def validate_maxAmount(self, value):
        if(value > 0):
            return value
        raise serializers.ValidationError('Max Amount must be greater than 0$')

class ListBidSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Bid
        fields =("__all__")
    nowDate = datetime.now().date()
    
    def validate_closeDate(self,value):
        if(self.nowDate > value):
            raise serializers.ValidationError('Close Date is prior to current date')
        return value
    def validate_maxAmount(self, value):
        if(value > 0):
            return value
        raise serializers.ValidationError('Max Amount must be greater than 0$')

class BidWithOffersSerializer(serializers.ModelSerializer):
    #Para que aparezcan los datos realizado en serializador los modelos Offerss y PostulacionBidTransporte en el columna Bid debe agregar related_name=""
    #Los modelos Ofertas related_name="offers" y  PostulacionBidTransporte related_name="postulations"
    offers = OfferSerializer(many=True,read_only=True)
    postulations= addTransportPostulationSerializer(many=True,read_only=True)
    class Meta:
        model= Bid
        fields= ("id",'name','description','country','region','city','street','postalCode','productList','maxAmount','processStatus','initDate','closeDate','international',"offers","postulations")


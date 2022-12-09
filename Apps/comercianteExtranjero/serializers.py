from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import *
from datetime import datetime
from django.utils import timezone
from Apps.productor.serializers import OfertaSerializer
from Apps.transportista.serializers import addPostulacionLicitacionSerializer

# It creates a serializer for the UserAccount model.
class LicitacionSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Licitacion
        fields = ('name','description','country','region','city','street','postalCode','productList','maxAmount','processStatus','initDate','closeDate','extranjero')
    
    nowDate = datetime.now().date()
    
    def validate_closeDate(self,value):
        if(self.nowDate > value):
            raise serializers.ValidationError('Fecha cierre es anterior a fecha de hoy')
        return value
    def validate_maxAmount(self, value):
        if(value > 0):
            return value
        raise serializers.ValidationError('El monto maximo debe ser mayor que 0$')

class ListLicitacionSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Licitacion
        fields =("__all__")

class LicitacionWithOfertaSerializer(serializers.ModelSerializer):
    #Para que aparescan los datos realizado en serializador los modelos Ofertas y PostulacionLicitacionTransporte en el columna licitacion debe agregar related_name=""
    #Los modelos Ofertas related_name="ofertas" y  PostulacionLicitacionTransporte related_name="postulaciones"
    ofertas = OfertaSerializer(many=True,read_only=True)
    postulaciones= addPostulacionLicitacionSerializer(many=True,read_only=True)
    class Meta:
        model= Licitacion
        fields= ("id",'name','description','country','region','city','street','postalCode','productList','maxAmount','processStatus','initDate','closeDate','extranjero',"ofertas","postulaciones")


from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import *
from datetime import datetime
from django.utils import timezone


# It creates a serializer for the UserAccount model.
class LicitacionSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Licitacion
        fields = ('name','description','country','region','city','street','postalCode','productList','maxAmount','processStatus','initDate','closeDate','extranjero')
    
    nowDate = datetime.now().date()

    def validate(self, data):
        if( data['closeDate'] > self.nowDate):
            if(data['maxAmount'] > 0):
                return data
            else:
                raise serializers.ValidationError('El monto maximo debe ser mayor que 0')    
        else :
            raise serializers.ValidationError('Fecha Cierre es anterior a fecha inicio')

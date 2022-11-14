from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import *
from django.utils import timezone


# It creates a serializer for the UserAccount model.
class SolicitudSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Solicitud
        fields = ('name','description','country','region','city','street','postalCode','productList','maxAmount','processStatus','initDate','closeDate')
    closeDate = serializers.DateTimeField()
    nowDate = timezone.now()

    def validate(self, data):
        if( data['closeDate'] > self.nowDate):
            
            return data
        else:
            raise serializers.ValidationError('Fecha Cierre es anterior a fecha inicio')

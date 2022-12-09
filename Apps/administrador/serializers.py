from dataclasses import fields
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
from .models import *

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ('type','companyName', 'initDate', 'endDate', 'fileName', 'isActive')

    nowDate = datetime.now().date()
    def validate(self, data):
        if( data['endDate'] > self.nowDate):
            
            return data
        else:
            raise serializers.ValidationError('Fecha Cierre es anterior a fecha inicio')

class UpdateContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        ##fields = ('id','type','companyName', 'initDate', 'endDate', 'fileName', 'isActive')
        fields = ('endDate')
    def validate(self, data):
        if( data['endDate'] > self.initDate):
            
            return data
        else:
            raise serializers.ValidationError('Fecha Cierre es anterior a fecha inicio')


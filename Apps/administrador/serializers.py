from dataclasses import fields
from rest_framework import serializers
from django.utils import timezone
from .models import *

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ('companyName', 'initDate', 'endDate', 'fileName')
    nowDate = timezone.now()
    def validate(self, data):
        if( data['endDate'] > self.nowDate):
            
            return data
        else:
            raise serializers.ValidationError('Fecha Cierre es anterior a fecha inicio')



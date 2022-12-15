from dataclasses import fields
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
from .models import *

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('type','companyName', 'initDate', 'endDate', 'file')

    nowDate = datetime.now().date()
    def validate(self, data):
        if( data['endDate'] > self.nowDate):
            
            return data
        else:
            raise serializers.ValidationError('Closing date is prior to start date')
            

class UpdatePdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id',"file")
        #fields = ("__all__")
    


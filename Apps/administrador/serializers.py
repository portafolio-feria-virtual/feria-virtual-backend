from dataclasses import fields
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
from .models import *

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('type','companyName', 'initDate', 'endDate', 'fileName', 'isActive')

    nowDate = datetime.now().date()
    def validate(self, data):
        if( data['endDate'] > self.nowDate):
            
            return data
        else:
            raise serializers.ValidationError('Closing date is prior to start date')

class UpdateContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        ##fields = ('id','type','companyName', 'initDate', 'endDate', 'fileName', 'isActive')
        fields = ('endDate')
    def validate(self, data):
        if( data['endDate'] > self.initDate):
            
            return data
        else:
            raise serializers.ValidationError('Close date is prior to start date')


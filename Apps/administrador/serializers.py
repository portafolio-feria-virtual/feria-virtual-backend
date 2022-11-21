from dataclasses import fields
from rest_framework import serializers
from .models import *

class CrearContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrearContrato
        fields = ('companyName', 'initDate', 'endDate', 'archiveName')


class VerContratoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = VerContrato
        fields = ('idContract', 'companyName', 'initDate', 'modifyDate', 'endDate', 'fileName')
        read_only_fields = ('idContract', 'companyName', 'initDate', 'fileName')

class VerProcesoVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerProcesoVentas
        fields = ('processName', 'description', 'endDate', 'country', 'regionState', 'city', 'street', 'postalCode', 'detail', 'processStatus')

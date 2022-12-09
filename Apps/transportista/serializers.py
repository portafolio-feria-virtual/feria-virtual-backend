from rest_framework import serializers
from .models import *
class addPostulacionLicitacionSerializer (serializers.ModelSerializer):
    class Meta:
        model = PostulacionLicitacionTransporte
        fields = ("__all__")


class envioSerializer (serializers.ModelSerializer):

    class Meta:
        model = Envio
        fields = ("__all__")
from dataclasses import fields
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    model = Oferta
    fields = ('name', 'description', 'productorDescription', 'offer', 'unitPrice','adminArchives', 'techArchives', 'economicArchives')


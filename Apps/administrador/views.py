from django.shortcuts import render
from rest_framework import status, generics
from rest_framework import permissions
from .serializers import *


# Create your views here.
class CrearContratoView(generics.CreateAPIView):
    premission_classes = (permissions.AllowAny,)
    serializer_class = CrearContratoSerializer

class VerContratoView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = VerContratoSerializer

class VerProcesoVentasView(generics.CreateAPIView):
    permssion_classes = (permissions.AllowAny,)
    serializer_class = VerProcesoVentasSerializer
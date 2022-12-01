from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, viewsets, permissions
from rest_framework.response import Response
from .serializers import *
from .models import *


# Create your views here.
class CrearContratoView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ContratoSerializer

class VerContratosView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get (self, request):
        contratos = Contrato.objects.all()
        serializer = ContratoSerializer(contratos, many=True)
        return Response(serializer.data)

class BuscarContratoView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post (self, request,):
        data = self.request.data
        companyName = data['companyName']
        contratos = Contrato.objects.get(companyName=companyName)
        serializer = ContratoSerializer(contratos)
        return Response(serializer.data)
    
        




from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics,permissions

# Create your views here.

class addPostulacionLicitacionView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class= addPostulacionLicitacionSerializer

class seeAllPostulaciones(APIView):
  permission_classes = [permissions.AllowAny]
  def get(self, request):
    data = self.request.data
    user = self.request.user
    postulaciones = PostulacionLicitacionTransporte.objects.all().filter(transportista= user.id)
    serializer = addPostulacionLicitacionSerializer(postulaciones, many = True)
    return Response(serializer.data)
class AceptarRechazarPostulacionTransporteView(APIView):
  """ Vista que permite aceptar o rechazar la postulación de transporte adjudicada por el transportista """
  permission_classes = [permissions.AllowAny]
  def post(self, request):
    data = self.request.data
    id = data["id"]
    postulacion = PostulacionLicitacionTransporte.objects.get(id=id)
    option = data["option"]
    if option=="Accept":
      postulacion.accepted = "ACCEPTED"
      postulacion.confirmed = True
    if option == "Reject":  
      postulacion.accepted= "REJECTED"
      postulacion.closed = True

class EstadoEnvioGeneralView(APIView):
  """ Metodo que retorna el estado del transporte/envio"""
  permission_classes = [permissions.AllowAny]
  def get(self, request):
    user = self.request.user
    envios = Envio.objects.all().filter(transportista= user.id)
    serializers = envioSerializer(envios, many=True)
    return Response(serializers.data)

class cambiarEstadoEnvioView(APIView):
  permission_classes = [permissions.AllowAny]
  estados = ["PREPARATION","AWAITING_CARRIER","RECEIVED_BY_CARRIER","ON_TRACK","RECEPTIONED"]
  def post(self, request):
    data = self.request.data
    user = self.request.user

    envio = Envio.objects.get(id =data["id"])
    if envio.status != "RECEPTIONED":
      indice = self.estados.index(envio.status)
      envio.status = self.estados[indice+1]
    
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics,permissions

# Create your views here.

class addPostulacionLicitacionView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class= addTransportPostulationSerializer

class SeeAllPostulations(APIView):
  permission_classes = [permissions.AllowAny]
  def get(self, request):
    data = self.request.data
    user = self.request.user
    postulations = TransportPostulation.objects.all().filter(transportista= user.id)
    serializer = addTransportPostulationSerializer(postulations, many = True)
    return Response(serializer.data)
class AcceptDeclineTransportPostulationView(APIView):
  """ Vista que permite aceptar o rechazar la postulación de transporte adjudicada por el transportista """
  permission_classes = [permissions.AllowAny]
  def post(self, request):
    data = self.request.data
    id = data["id"]
    postulation = TransportPostulation.objects.get(id=id)
    option = data["option"]
    if option=="Accept":
      postulation.accepted = "ACCEPTED"
      postulation.confirmed = True
    if option == "Decline":  
      postulation.accepted= "DECLINED"
      postulation.closed = True

class ShippingStatusGeneralView(APIView):
  """ Metodo que retorna el estado del transporte/envio"""
  permission_classes = [permissions.AllowAny]
  def get(self, request):
    user = self.request.user
    envios = Shipping.objects.all().filter(transportista= user.id)
    serializers = ShippingSerializer(envios, many=True)
    return Response(serializers.data)

class UpdateShippingStatusView(APIView):
  permission_classes = [permissions.AllowAny]
  stages = ["PREPARATION","AWAITING_CARRIER","RECEIVED_BY_CARRIER","ON_TRACK","RECEPTIONED"]
  def post(self, request):
    data = self.request.data
    user = self.request.user

    shipping = Shipping.objects.get(id =data["id"])
    if shipping.status != "RECEPTIONED":
      index = self.stages.index(shipping.status)
      shipping.status = self.stages[index+1]
    
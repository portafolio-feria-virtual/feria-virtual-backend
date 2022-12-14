from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics,permissions, status
from Apps.comercianteExtranjero.models import *
from Apps.comercianteExtranjero.serializers import *

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

class ListAllBidsAvailablesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            bids = Bid.objects.all().filter(closed= False)
            return Bid(bids, many=True)

        except:
            return Response(status.HTTP_400_BAD_REQUEST)

class UpdateTransportPostulation(generics.UpdateAPIView):
    '''Modificar datos de una Bid segun id Bid'''
    permission_classes = (permissions.AllowAny, )


    queryset = TransportPostulation.objects.all()
    serializer_class = addTransportPostulationSerializer

    def get_object(self):
        data = self.request.data
        return TransportPostulation.objects.filter(id = data["id"]).first()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Offer modified"}, status.HTTP_200_OK)

        else:
            return Response({"message": "failed", "details": serializer.errors},status.HTTP_400_BAD_REQUEST)
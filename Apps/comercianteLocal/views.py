from django.shortcuts import render
from .serializers import *
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import permissions
from Apps.productor.models import *
from rest_framework.response import Response
from Apps.productor.serializers import *

# Create your views here.
class CreateBuyingOfferView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BuyingOfferSerializer


class ListAllSalesAvailablesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            sales = LocalSale.objects.all().filter(sold = False)
            serializer = LocalSaleSerializer(sales, many=True)
            return Response(serializer.data, status.HTTP_200_OK)

        except:
            return Response(status.HTTP_400_BAD_REQUEST)
class ListAllBuyOffersView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            buyOffers = BuyingOffer.objects.all().filter(localTrader= self.request.user.id)
            serializer = BuyingOfferSerializer(buyOffers, many=True)
            return Response(serializer.data, status.HTTP_200_OK)

        except:
            return Response(status.HTTP_400_BAD_REQUEST)

class UpdateBuyOffer(generics.UpdateAPIView):
    '''Modificar datos de una Bid segun id Bid'''
    permission_classes = (permissions.AllowAny, )


    queryset = BuyingOffer.objects.all()
    serializer_class = BuyingOfferSerializer

    def get_object(self):
        data = self.request.data
        return BuyingOffer.objects.filter(id = data["id"]).first()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Offer modified"}, status.HTTP_200_OK)

        else:
            return Response({"message": "failed", "details": serializer.errors},status.HTTP_400_BAD_REQUEST)

class CloseBuyOfferView(APIView):
  permission_classes = (permissions.AllowAny, )
  def post(self, request):
    data = self.request.data
    user = self.request.user
    try:
      buyOffer = BuyingOffer.objects.get(id = data["id"])
      buyOffer.status = "FINISHED"
      buyOffer.editable = False
      serializer = BuyingOfferSerializer(buyOffer)
      return Response(serializer.data)
    except:
      return Response(status.HTTP_400_BAD_REQUEST)

class AcceptDeclineSaleAssignmentView(APIView):
  """ Vista que permite aceptar o rechazar la licitación que se ha adjudicado el productor"""
  
  permission_classes = [permissions.AllowAny]
  
  def post(self, request):

    data = self.request.data
    id = data["id"]
    try:
      buyOffer = BuyingOffer.objects.get(id=id)
      opt = data["opt"]
      if opt=="Accept":
        buyOffer.status = "ACCEPTED"
        buyOffer.editable = False
        buyOffer.confirmed = True

        
      if opt == "Decline":  
        buyOffer.status = "REJECTED"
        buyOffer.editable = False
        buyOffer.confirmed = False

      serializer = BuyingOfferSerializer(buyOffer)
      return Response(serializer.data)
    except:
      return Response(status.HTTP_400_BAD_REQUEST)
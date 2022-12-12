from django.shortcuts import render
from .serializers import *
from Apps.productor.serializers import OfferSerializer
from Apps.productor.models import Offer
from Apps.transportista.serializers import addTransportPostulationSerializer,ShippingSerializer
from Apps.transportista.models import TransportPostulation, Shipping
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth.decorators import user_passes_test
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from datetime import datetime
from Apps.productor.models import Offer
from Apps.productor.serializers import OfferSerializer
from Apps.transportista.models import  *


# @user_passes_test(check_type)
class BidView(UserPassesTestMixin, generics.CreateAPIView):
    def test_func(self):
        print(self.request.user.type)
        return self.request.user.type == "INTERNATIONAL TRADER"


    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = BidSerializer

class AddBidView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = BidSerializer

class SearchBidView(APIView):
    ''' Obtener una Bid segun id de la Bid '''
    permission_classes = (permissions.AllowAny, )
    #serializer_class = BidSerializer
    def post(self,request):
        data = self.request.data
        id = data["id"]
        bid = Bid.objects.get(id= id)
        serializers = BidSerializer(bid)
        return Response(serializers.data)

class ListBidView(APIView):
    '''Obtiene un lista Bides segun el id del extranjero tenga Bides '''
    permission_classes = (permissions.AllowAny, )
    def get(self,request):
        data = self.request.data
        internationalTrader = data["internatialTrader"]   
        bids = Bid.objects.filter(internationalTrader= internationalTrader)
        serializer = BidWithOffersSerializer(bids, many=True)
        return Response(serializer.data)

class ListOffersProductorView(APIView):
    ''' Obtener lista ofertas segun id Bid en la oferta '''
    permission_classes = (permissions.AllowAny, )
    def get(self,request):
        data = self.request.data
        bid = data["bid"]   
        offers = Offer.objects.filter(Bid=bid)
        serializers = OfferSerializer(offers,many=True)
        return Response(serializers.data)

class ListCarriersPostulationView(APIView):
    ''' Obtener lista ofertas segun id Bid en la postulacion transportista '''
    permission_classes = (permissions.AllowAny, )
    def get(self,request):
        data = self.request.data
        bid = data["bid"]
        postulations = TransportPostulation.objects.filter(Bid=bid)
        serializers = addTransportPostulationSerializer(postulations,many=True)
        return Response(serializers.data)

class EditCloseDateView(APIView):
    ''' Obtener lista Bid segun id Bid '''
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        data = self.request.data
        id = data["id"]
        closeDate = datetime.strptime(data["closeDate"],'%d/%m/%Y').date()
        nowDate = datetime.now().date()
        bid = Bid.objects.filter(id= id).first()
        hasOffer = Offer.objects.filter(bid=id).count()
        if(hasOffer == 0):           
            if nowDate < closeDate:
                bid.closeDate = closeDate
                bid.save()
                return Response({"message": "Bid Date modified."})
            else:
                return Response({"message": "Close date must be after current date."})
        else:
            return Response({"message": "Can't extend close date, Bid has offers related."})

class UpdateBid(UpdateAPIView):
    '''Modificar datos de una Bid segun id Bid'''
    permission_classes = (permissions.AllowAny, )


    queryset = Bid.objects.all()
    serializer_class = ListBidSerializer

    def get_object(self):
        data = self.request.data
        return Bid.objects.filter(id = data["id"]).first()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bid modified"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
            
class AcceptDeclineOfferProducerView(APIView):
    ''' Accept an offer made by the producer, searching the offer by id an marking it as assigned= True '''
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        data = self.request.data
        id = data["id"]
        status = data["status"]
        offer = Offer.objects.get(id= id)
        if status == "Accepted":
            offer.assigned = True
            offer.status = status
            offer.save()
            return Response({"message": "Offer accepted"})
        elif status == "Rejected":
            offer.assigned = False
            offer.status = status
            offer.save()
            return Response({"message": "Offer rejected"})
        else:
           return Response({"message": "Offer action not resolved"})

class AcceptDeclineTransportPostulationView(APIView):
    ''' Obtener lista Bid segun id Bid '''
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        data = self.request.data
        id = data["id"]
        status = data["status"]
        postulation = TransportPostulation.objects.get(id= id)
        if status == "Accepted":
            postulation.assigned = True
            postulation.accepted = status
            postulation.save()
            return Response({"message": "Transport postulation accepted"})
        elif status == "Rejected":
            postulation.assigned = False
            postulation.accepted = status
            postulation.save()
            return Response({"message": "Transport Postulation rejected"})
        else:
           return Response({"message": "Action not perfomed, petition cannot be resolved"})

class ShippingStatusBidView(APIView):
    ''' Obtener un Envio segun id de la Bid '''
    permission_classes = (permissions.AllowAny, )
    def get(self,request):
        data = self.request.data
        bid = data["bid"]
        shippingBid = Shipping.objects.filter(bid=bid).first()
        serializers = ShippingSerializer(shippingBid)
        return Response(serializers.data)




class SeeAllBidWithOfferView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = BidWithOffersSerializer

    def get(self, request):
        Bid = Bid.objects.all().filter(extranjero= self.request.user.id)
        serializer = self.serializer_class(Bid, many=True)
        return Response(serializer.data)



    



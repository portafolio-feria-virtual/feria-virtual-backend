from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from .serializers import *
from .models import *
from Apps.comercianteExtranjero.models import Bid
from Apps.comercianteExtranjero.serializers import BidSerializer
from Apps.productor.models import Offer
from Apps.productor.serializers import OfferSerializer
from Apps.productor.models import LocalSale
from Apps.productor.serializers import LocalSaleSerializer

# Create your views here.
class CreateContractView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ContractSerializer

class SeeAllContractsView(APIView):
    permission_classes = (permissions.AllowAny,)
    #serializer_class = ContractSerializer
    def get (self, request):
        Contracts = Contract.objects.all()
        serializer = ContractSerializer(Contracts, many=True)
        return Response(serializer.data)

class SearchContractView(APIView):
    permission_classes = (permissions.AllowAny,)
    #serializer_class =ContractSerializer
    def post (self, request,):
        data = self.request.data
        companyName = data['companyName']
        Contracts = Contract.objects.get(companyName=companyName)
        serializer = ContractSerializer(Contracts)
        return Response(serializer.data)

class EditDateContractView(APIView):
    ##serializer_class = UpdateContractSerializer
    permission_classes = (permissions.AllowAny,)

    def patch(self, request):

        data = self.request.data
        ##print(data['id'])
        id = data['id']
        Contract = Contract.objects.get(id=id)
        Contract.endDate = data['endDate']
        serializer = ContractSerializer(Contract)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class EditPdfContractView(APIView):
    serializer_class = UpdatePdfSerializer
    permission_classes = (permissions.AllowAny,)

    def patch(self, request):

        data = self.request.data
        ##print(data['id'])
        id = data['id']
        contract = Contract.objects.get(id=id)
        contract.file = self.request.FILES["file"]
        serializer = ContractSerializer(contract)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SeeAllBidsView(APIView):
    permission_classes = (permissions.AllowAny, )
    #serializer_class = BidSerializer
    def get (self, request):
        bid = Bid.objects.all()
        serializer = BidSerializer(bid, many=True)
        return Response(serializer.data)
        
class SeeAllOffersView(APIView):
    permission_classes = (permissions.AllowAny,)
    #serializer_class = OfertaSerializer
    def get(self, request):
        offer = Offer.objects.all()
        serializer = OfferSerializer(offer, many=True)
        return Response(serializer.data)

class SeeAllLocalSalesView(APIView):
    permission_classes = (permissions.AllowAny,)
    #serializer_class = VentaLocalSerializer
    def get(self, request):
        def get(self, request):
            localSale = LocalSale.objects.all()
            serializer = LocalSaleSerializer(localSale, many=True)
            return Response(serializer.data)


class CloseContractView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        data = self.request.data
        user = self.request.user
        try:
            contract = Contract.objects.get(data["id"])
            contract.isActive = False
            contract.save()
        except:
            return Response(status.HTTP_400_BAD_REQUEST)
# class UpdateContract(UpdateAPIView):
#     '''Modificar datos de una Bid segun id Bid'''
#     permission_classes = (permissions.AllowAny, )


#     queryset = Bid.objects.all()
#     serializer_class = ListBidSerializer

#     def get_object(self):
#         data = self.request.data
#         return Bid.objects.filter(id = data["id"]).first()

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Bid modified"})

#         else:
#             return Response({"message": "failed", "details": serializer.errors})
            
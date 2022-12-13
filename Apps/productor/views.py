from django.shortcuts import render
from PIL import Image
import pyrebase
import os
# Create your views here.
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.conf import settings
import urllib.parse
import json

from Apps.transportista.models import *
from rest_framework.parsers import FileUploadParser, MultiPartParser,FormParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import permissions, viewsets
from .serializers import *
from Apps.transportista.models import *
from Apps.transportista.serializers import *
import uuid




config = {
  "apiKey": "AIzaSyAqGaP1ePwNe3G4ndQC39owYaENlGB8itY",
  "authDomain": "bucket-portafolio.firebaseapp.com",
  "projectId": "bucket-portafolio",
  "storageBucket": "bucket-portafolio.appspot.com",
  "messagingSenderId": "470955898689",
  "appId": "1:470955898689:web:9419cfd8e1e9da78d613c0",
  "measurementId": "G-9M85SHKCEV",
  "databaseURL":"gs://bucket-portafolio.appspot.com",
 #"serviceAccount":"Apps/productor/bucket-portafolio-firebase-adminsdk-gii80-6c536b1389.json"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
storage.child()

# Create your views here.
class AddOfferView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = OfferSerializer

class SeeAllOfferView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = OfferSerializer

    def get(self, request):
      try:
        offers = Offer.objects.all().filter(producer= self.request.user.id)
        serializador = self.serializer_class(offers, many=True)
        return Response(serializador.data)
      except:
        return Response(status.HTTP_400_BAD_REQUEST)

class SeeAllLocalSalesView(APIView):
  permission_classes = (permissions.AllowAny, )
  serializer_class = LocalSale

  def get(self, request):
    try:
      sales = LocalSale.objects.all().filter(producer= self.request.user.id)
      serializer = self.serializer_class(sales, many=True)
      return Response(serializer.data)
    except:
      return Response(status.HTTP_400_BAD_REQUEST)

class SearchSaleView(APIView):
  permission_classes = (permissions.AllowAny, )
  #serializer_class = LocalSaleSerializer
  def post(self, request):
    data = self.request.data
    user = self.request.user
    try:
      lSale = LocalSale.objects.get(id = data['id'])
      serializer = LocalSaleSerializer(lSale)
      return Response(serializer.data)
    except:
      return Response(status.HTTP_400_BAD_REQUEST)

class CloseSaleView(APIView):
  permission_classes = (permissions.AllowAny, )
  def post(self, request):
    data = self.request.data
    user = self.request.user
    try:
      lSale = LocalSale.objects.get(id = data["id"])
      lSale.status = "CLOSED"
      lSale.closed = True
      serializer = LocalSaleSerializer(lSale)
      return Response(serializer.data)
    except:
      return Response(status.HTTP_400_BAD_REQUEST)
class CancelOfferView(APIView):
  permission_classes = (permissions.AllowAny, )
  def post(self, request):
    data = self.request.data
    user = self.request.user
    try:
      offer = Offer.objects.get(id = data["id"])

      offer.closed = True
      serializer = LocalSaleSerializer(offer)
      return Response(serializer.data)
    except:
      return Response(status.HTTP_400_BAD_REQUEST)

class SearchOfferView(APIView):
  permission_classes = (permissions.AllowAny, )
  serializer_class = OfferSerializer
  def post(self, request):
    data = self.request.data
    user = self.request.user
    try:
      lSale = Offer.objects.get(id=data["id"])
      serializer = self.serializer_class(lSale)
      return Response(serializer.data)
    except:
      return Response(status.HTTP_400_BAD_REQUEST)



class CreateLocalSaleView(generics.CreateAPIView):
  permission_classes = (permissions.AllowAny, )
  serializer_class = AddLocalSaleSerializer

class LocalSaleImageView(generics.CreateAPIView):
  model = LocalSaleImage
  permission_classes = [permissions.AllowAny]
  serializer_class = LocalSaleImageSerializer

  # def perform_create(self, serializer):
  #   fs = FileSystemStorage()
  #   data = self.request.data
  #   file = self.request.FILES['image']
  #   localSale = LocalSale.objects.get(id=data["ventaLocal"])
  #   producer = Producer.objects.get(id=localSale.producer.id)
  #   print(LocalSale)
  #   print(file)
  #   filename = fs.save(file.name, file)
  #   file_url = fs.url(filename)
  #   print(filename)
  #   print(file_url)
  #   storage.child("files/" + producer.businessName+"/"+localSale.name+"/"+str(uuid.uuid4())).put("media/" + file.name)
  #   serializer.save()   
  def perform_create(self, serializer):
    
    data = self.request.data
    try:
      file = self.request.FILES["image"]
    except:
      file = None
    
    localSale = LocalSale.objects.get(id=data["localSale"])
    producer = Producer.objects.get(id=localSale.producer.id)
    if localSale and producer:
      if not file == None:
        file._name= str(uuid.uuid4())+"."+file._name.split('.')[1]
        fs = FileSystemStorage("media/localSales/" + producer.businessName+"/"+localSale.name+"/")
        
        filename = fs.save(file.name, file)
        print(filename)
        # file_url = fs.url(filename)
        serializer.save(localSale=localSale, image= f"localSales/{producer.businessName}/{localSale.name}/{filename}")
        return Response(status.HTTP_200_OK)
      else: 
        return Response({"message":"please, provide a file"},status.HTTP_400_BAD_REQUEST)
        



# class RetrieveImagesView(APIView):
#   model = ImagenVentaLocal
#   permission_classes = [permissions.AllowAny]

#   def get(self,request):
#     all_files = storage.child("/files/Caracolas/Venta de caracolas").list_files()
#     print(all_files)
#     archivos = {}
#     for idx, file in enumerate(all_files):
#       try:
#         print(file.name)
       
#         z = storage.child(file.name).get_url(None)
#         archivos[idx] = str(z)
#         print(f"imprimiendo {z} ")

#       except:
#         print("retrieve failed")
#     return Response(archivos)

class RetrieveImagesView(APIView):
  model = LocalSaleImage
  # serializer_class = LocalSaleImageSerializer
  permission_classes = [permissions.AllowAny]
  def post(self, request):
    data = self.request.data
    localSale = LocalSale.objects.get(id=data["localSale"])
    images = self.model.objects.all().filter(localSale=localSale)
    archivos = {}
    try:
      for idx, image in enumerate(images):
        temp = image.image.url
        archivos[idx] = request.build_absolute_uri(image.image.url)
        #archivos[idx]= RetrieveLocalSaleImageSerializer(image).data
      
      return Response(archivos, status.HTTP_200_OK)

    except:
        return Response(status.HTTP_400_BAD_REQUEST)


class AcceptDeclineAssignmentView(APIView):
  """ Vista que permite aceptar o rechazar la licitación que se ha adjudicado el productor"""
  
  permission_classes = [permissions.AllowAny]
  
  def post(self, request):

    data = self.request.data
    id = data["id"]
    try:
      offer = Offer.objects.get(id=id)
      option = data["option"]
      if option=="Accept":
        offer.status = "ACCEPTED"
        offer.confirmed= True
      if option == "Decline":  
        offer.Status = "REJECTED"
        offer.closed = True

      serializer = OfferSerializer(offer)
      return Response(serializer.data)
    except:
      return Response(status.HTTP_400_BAD_REQUEST)


    

class ShippingStatusGeneralView(APIView):
  """ Metodo que retorna el estado del transporte/envio"""
  permission_classes = [permissions.AllowAny]
  def get(self, request):
    user = self.request.user
    shippings = Shipping.objects.all().filter(producer=user.id).exclude(status="PREPARATION")
    serializers = ShippingSerializer(shippings, many=True)

    return Response(serializers.data)
class ShippingStatusProducerView(APIView):
  """ Metodo que retorna el estado del transporte/envio"""
  permission_classes = [permissions.AllowAny]
  def get(self, request):
    user = self.request.user
    shippings = Shipping.objects.all().filter(producer= user.id, status="PREPARATION")
    serializers = ShippingSerializer(shippings, many=True)

    return Response(serializers.data)

class MarkShipping(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    data = self.request.data
    user = self.request.user

    envio = Shipping.objects.get(id =data["id"])
    if envio:
      envio.status = "AWAITING CARRIER"
      envio.save()
      return Response(status.HTTP_200_OK)
    else:
      return Response(status.HTTP_400_BAD_REQUEST)



    serializer = OfferSerializer(offer)
    return Response(serializer.data)

class RestockLocalSale(APIView):
  model = LocalSale
  serializer_class = LocalSaleSerializer
  permission_classes = [permissions.AllowAny]

  def patch(self, request):
    data = self.request.data
    lSale = LocalSale.objects.get(id=data["id"])
    if lSale:

      lSale.stock = data["stock"]
      lSale.save()
      return Response(status.HTTP_200_OK)
    else:
      return Response(status.HTTP_404_NOT_FOUND)


class SeeAllSalesWithBuyingOfferView(APIView):

  permission_classes = (permissions.AllowAny, )
  serializer_class = SeeAllSalesWithBuyingOfferSerializer

  def get(self, request):
    try:
      lSale= LocalSale.objects.all().filter(producer= self.request.user.id)
      serializer = self.serializer_class(lSale, many=True)
      return Response(serializer.data)
    except:
      return Response(status.HTTP_400_BAD_REQUEST)
  
class AcceptDeclineSaleOffer(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    try:
      data = self.request.data
      id = data["id"]
      buyOffer = BuyingOffer.objects.get(id=id)
      lSale = LocalSale.objects.get(id=buyOffer.localSale)
      option = data["option"]
      if option=="Accept":
        
        buyOffer.editable = False
        buyOffer.status = "FINISHED"
        lSale.stock = lSale.stock - buyOffer.quantity
        lSale.save()
        buyOffer.save()
      if option == "Decline":  
        buyOffer.status = "FINISHED"
        buyOffer.editable = False
        buyOffer.save()
    except:
      return Response(status.HTTP_400_BAD_REQUEST)

class UpdateOffer(generics.UpdateAPIView):
    '''Modificar datos de una Bid segun id Bid'''
    permission_classes = (permissions.AllowAny, )


    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_object(self):
        data = self.request.data
        return Offer.objects.filter(id = data["id"]).first()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Offer modified"}, status.HTTP_200_OK)

        else:
            return Response({"message": "failed", "details": serializer.errors},status.HTTP_400_BAD_REQUEST)
class UpdateSale(generics.UpdateAPIView):
    '''Modificar datos de una Bid segun id Bid'''
    permission_classes = (permissions.AllowAny, )


    queryset = LocalSale.objects.all()
    serializer_class = LocalSaleSerializer

    def get_object(self):
        data = self.request.data
        return LocalSale.objects.filter(id = data["id"]).first()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Offer modified"}, status.HTTP_200_OK)

        else:
            return Response({"message": "failed", "details": serializer.errors},status.HTTP_400_BAD_REQUEST)
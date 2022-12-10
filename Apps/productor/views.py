from django.shortcuts import render
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
class OfertaView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = OfertaSerializer

class SeeAllOfferView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = OfertaSerializer

    def get(self, request):
        ofertas = Oferta.objects.all().filter(productor= self.request.user.id)
        serializador = self.serializer_class(ofertas, many=True)
        return Response(serializador.data)


class VentaLocalCreateView(generics.CreateAPIView):
  permission_classes = (permissions.AllowAny, )
  serializer_class = VentaLocalSerializer

class ImagenVentaLocalView(generics.CreateAPIView):
  model = ImagenVentaLocal
  permission_classes = [permissions.AllowAny]
  serializer_class = ImageSerializer

  def perform_create(self, serializer):
    fs = FileSystemStorage()
    data = self.request.data
    file = self.request.FILES['image']
    ventaLocal = VentaLocal.objects.get(id=data["ventaLocal"])
    productor = Productor.objects.get(id=ventaLocal.productor.id)
    print(ventaLocal)
    print(file)
    filename = fs.save(file.name, file)
    file_url = fs.url(filename)
    print(filename)
    print(file_url)
    storage.child("files/" + productor.businessName+"/"+ventaLocal.name+"/"+str(uuid.uuid4())).put("media/" + file.name)
    serializer.save()   
  
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

class AceptarRechazarAdjudicacionView(APIView):
  """ Vista que permite aceptar o rechazar la licitación que se ha adjudicado el productor"""
  
  permission_classes = [permissions.AllowAny]
  
  def post(self, request):

    data = self.request.data
    id = data["id"]
    oferta = Oferta.objects.get(id=id)
    option = data["option"]
    if option=="Accept":
      oferta.accepted = "ACCEPTED"
      oferta.confirmed= True
    if option == "Reject":  
      oferta.accepted = "REJECTED"
      oferta.closed = True

    serializer = OfertaSerializer(oferta)
    return Response(serializer.data)


    

class EstadoEnvioGeneralView(APIView):
  """ Metodo que retorna el estado del transporte/envio"""
  permission_classes = [permissions.AllowAny]
  def get(self, request):
    user = self.request.user
    envios = Envio.objects.all().filter(productor= user.id).exclude(status="PREPARATION")
    serializers = envioSerializer(envios, many=True)

    return Response(serializers.data)
class EstadoEnvioProductorView(APIView):
  """ Metodo que retorna el estado del transporte/envio"""
  permission_classes = [permissions.AllowAny]
  def get(self, request):
    user = self.request.user
    envios = Envio.objects.all().filter(productor= user.id, status="PREPARATION")
    serializers = envioSerializer(envios, many=True)

    return Response(serializers.data)

class MarcarEnvio(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    data = self.request.data
    user = self.request.user

    envio = Envio.objects.get(id =data["id"])
    envio.status = "AWAITING CARRIER"



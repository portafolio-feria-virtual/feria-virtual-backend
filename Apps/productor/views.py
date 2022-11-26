from django.shortcuts import render
import pyrebase
import os
# Create your views here.
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.contrib import messages
from django.conf import settings

from rest_framework.parsers import FileUploadParser, MultiPartParser,FormParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import permissions, viewsets
from .serializers import *




config = {
  "apiKey": "AIzaSyAqGaP1ePwNe3G4ndQC39owYaENlGB8itY",
  "authDomain": "bucket-portafolio.firebaseapp.com",
  "projectId": "bucket-portafolio",
  "storageBucket": "bucket-portafolio.appspot.com",
  "messagingSenderId": "470955898689",
  "appId": "1:470955898689:web:9419cfd8e1e9da78d613c0",
  "measurementId": "G-9M85SHKCEV",
  "databaseURL":"gs://bucket-portafolio.appspot.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
storage.child()
# Create your views here.
class OfertaView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = OfertaSerializer


# class VentaLocalView(generics.CreateAPIView):
#     permission_classes = (permissions.AllowAny, )
#     serializer_class= VentaLocalSerializer



# class VentaLocalView(APIView):
#     form_class = VentaLocalForm
#     # A class that is used to parse the file.
#     #parser_classes = (FileUploadParser)

#     def post(self, request, format=None):
#         serializer = VentaLocalSerializer(data=request.data)
#         file = request.FILES['file']
#         file_save = default_storage.save(file.name, file)
#         storage.child("files/" + file.name).put("media/" + file.name)
#         delete = default_storage.delete(file.name)

#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@method_decorator(csrf_exempt, name='dispatch')
class VentaLocalViewSet(viewsets.ModelViewSet):
        queryset = VentaLocal.objects.all()
        serializer_class = VentaLocalSerializer
        permission_classes = [permissions.AllowAny]
        http_method_names = ["post","get"]

        def create(self, request, *args, **kwargs):
          images = request.FILES.getlist('image', None)
          data = {
            "productor": request.POST.get("productor",None),
            "name": request.POST.get("name",None),
            "price": request.POST.get("price",None),
            "stock": request.POST.get("stock",None),
            "location": request.POST.get("location",None),
          }
          _serializer = self.serializer_class(data =data, context ={'images':images})
          if _serializer.is_valid():
            _serializer.save()
            return Response(data=_serializer.data, status=status.HTTP_201_CREATED)
          else:
            return Response(data=_serializer.erors, status = status.HTTP_400_BAD_REQUEST)

        # def perform_create(self, serializer):
        #     file = self.request.FILES['image']
        #     default_storage.save(file.name, file)
        #     storage.child("files/" + file.name).put("media/" + file.name)
        #     print(file.name)
        #     default_storage.delete(file.name)
        # #     serializer.save()
        # def perform_create(self, serializer):

        #   for f in self.request.data.getList("image"):
        #     default_storage.save(f.name, f)
        #     storage.child("files/" +self.request.data["productor"]+self.request.data["name"] +f.name).put("media/" + f.name)
        #     print(f.name)
        #     default_storage.delete(f.name)
        #     serializer.save()
            
            
# class VentaLocalView(APIView):

#   parser_classes = (MultiPartParser, FormParser)
#   permission_classes = [permissions.AllowAny]

#   def post(self, request):
#     data = self.request.data
#     file = self.request.FILES["image"]
#     default_storage.save(file.name, file)
#     storage.child("files/" + file.name).put("media/" + file.name)
#     print(file.name)
#     print(default_storage.exists(file.name))
#     default_storage.delete(file.name)
#     serializers = VentaLocalSerializer()
#     serializer.save()


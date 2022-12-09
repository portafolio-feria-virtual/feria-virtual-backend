from django.shortcuts import render
from .serializers import *
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import permissions
# Create your views here.
class CrearSolicitudCompraView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SolicitudCompraSerializer
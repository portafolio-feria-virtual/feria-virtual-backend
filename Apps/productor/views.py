from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework import permissions
from .serializers import *

# Create your views here.
class OfertaView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = OfertaSerializer
from django.shortcuts import render
from rest_framework import status, generics
from .serializers import *

# Create your views here.
# class SignupView(generics.CreateAPIView):
#     serializer_class = UserSerializer

class ExtranjeroSignupView(generics.CreateAPIView):
    serializer_class = ComercianteExtranjeroSignupSerializer

class LocalSignupView(generics.CreateAPIView):
    serializer_class = ComercianteLocalSignupSerializer

class ProductorSignupView(generics.CreateAPIView):
    serializer_class = ProductorSignupSerializer

class TransportistaSignupView(generics.CreateAPIView):
    serializer_class = TransportistaSignupSerializer
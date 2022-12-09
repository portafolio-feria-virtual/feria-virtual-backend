from django.shortcuts import render
from .serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth.decorators import user_passes_test
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Apps.productor.models import Oferta
from Apps.productor.serializers import OfertaSerializer
from Apps.transportista.models import  *


# def check_type(user):
#     return user.type == "transportista"


# @user_passes_test(check_type)
class LicitacionView(UserPassesTestMixin, generics.CreateAPIView):
    def test_func(self):
        print(self.request.user.type)
        return self.request.user.type == "COMERCIANTE EXTRANJERO"


    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LicitacionSerializer

class AddLicitacionView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = LicitacionSerializer

class SearchLicitacionView(APIView):
    ''' Obtener lista licitacion segun id licitacion '''
    permission_classes = (permissions.AllowAny, )
    #serializer_class = LicitacionSerializer
    def post(self,request):
        data = self.request.data
        id = data["id"]
        licitacion = Licitacion.objects.get(id= id)
        serializers = LicitacionSerializer(licitacion)
        return Response(serializers.data)


class SeeAllLicitacionWithOfferView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = LicitacionWithOfertaSerializer

    def get(self, request):
        licitacion = Licitacion.objects.all().filter(extranjero= self.request.user.id)
        serializador = self.serializer_class(licitacion, many=True)
        return Response(serializador.data)


class AsignarRechazarOfertaLicitacion(APIView):
  """ Vista que permite asignar o rechazar la oferta que ha recibido una licitación """
  permission_classes = [permissions.AllowAny]
  def post(self, request):
    data = self.request.data
    id = data["id"]
    oferta = Oferta.objects.get(id=id)
    option = data["option"]
    if option=="Accept":
      oferta.assigned = True
      oferta.accepted = "ACCEPTED"
    if option == "Reject":  
      oferta.assigned= False
      oferta.accepted = "REJECTED"
      oferta.closed= True

    




    



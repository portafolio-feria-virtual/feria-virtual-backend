from django.shortcuts import render
from .serializers import *
from Apps.productor.serializers import OfertaSerializer
from Apps.productor.models import Oferta
from Apps.transportista.serializers import addPostulacionLicitacionSerializer,envioSerializer
from Apps.transportista.models import PostulacionLicitacionTransporte,Envio
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
from Apps.productor.models import Oferta
from Apps.productor.serializers import OfertaSerializer
from Apps.transportista.models import  *


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
    ''' Obtener una licitacion segun id de la licitacion '''
    permission_classes = (permissions.AllowAny, )
    #serializer_class = LicitacionSerializer
    def post(self,request):
        data = self.request.data
        id = data["id"]
        licitacion = Licitacion.objects.get(id= id)
        serializers = LicitacionSerializer(licitacion)
        return Response(serializers.data)

class ListLicitacionView(APIView):
    '''Obtiene un lista licitaciones segun el id del extranjero tenga licitaciones '''
    permission_classes = (permissions.AllowAny, )
    def get(self,request,extranjero):
        licitaciones = Licitacion.objects.filter(extranjero= extranjero)
        serializer = LicitacionWithOfertaSerializer(licitaciones, many=True)
        return Response(serializer.data)

class ListOfertaProductorView(APIView):
    ''' Obtener lista ofertas segun id licitacion en la oferta '''
    permission_classes = (permissions.AllowAny, )
    def get(self,request,licitacion):
        ofertas = Oferta.objects.filter(licitacion=licitacion)
        serializers = OfertaSerializer(ofertas,many=True)
        return Response(serializers.data)

class ListPostulacionTransportistaView(APIView):
    ''' Obtener lista ofertas segun id licitacion en la postulacion transportista '''
    permission_classes = (permissions.AllowAny, )
    def get(self,request,licitacion):
        postulaciones = PostulacionLicitacionTransporte.objects.filter(licitacion=licitacion)
        serializers = addPostulacionLicitacionSerializer(postulaciones,many=True)
        return Response(serializers.data)

class EditCloseDateView(APIView):
    ''' Obtener lista licitacion segun id licitacion '''
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        data = self.request.data
        id = data["id"]
        closeDate = datetime.strptime(data["closeDate"],'%d/%m/%Y').date()
        nowDate = datetime.now().date()
        licitacion = Licitacion.objects.filter(id= id).first()
        hayOferta = Oferta.objects.filter(licitacion=id).count()
        if(hayOferta == 0):           
            if nowDate < closeDate:
                licitacion.closeDate = closeDate
                licitacion.save()
                return Response({"message": "fecha licitacion modificada"})
            else:
                return Response({"message": "La fecha cierre debe ser mayor que fecha de hoy"})
        else:
            return Response({"message": "La fecha de cierre no puede extenderse hay ofertas existente en la licitacion"})

class UpdateLicitacion(UpdateAPIView):
    '''Modificar datos de una licitacion segun id licitacion'''
    permission_classes = (permissions.AllowAny, )


    queryset = Licitacion.objects.all()
    serializer_class = LicitacionSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Licitacion modificada"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
            
class AceptarRechazarOfertaProductorView(APIView):
    ''' Obtener lista licitacion segun id licitacion '''
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        data = self.request.data
        id = data["id"]
        estado = data["status"]
        oferta = Oferta.objects.get(id= id)
        if estado == "Accepted":
            oferta.assigned = True
            oferta.accepted = estado
            oferta.save()
            return Response({"message": "Oferta Aceptada"})
        elif estado == "Rejected":
            oferta.assigned = False
            oferta.accepted = estado
            oferta.save()
            return Response({"message": "Oferta Rechazada"})
        else:
           return Response({"message": "Accion de oferta no realizada"})

class AceptarRechazarPostulacionTrasporteView(APIView):
    ''' Obtener lista licitacion segun id licitacion '''
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        data = self.request.data
        id = data["id"]
        estado = data["status"]
        postulacion = PostulacionLicitacionTransporte.objects.get(id= id)
        if estado == "Accepted":
            postulacion.assigned = True
            postulacion.accepted = estado
            postulacion.save()
            return Response({"message": "Postulacion de transporte aceptada"})
        elif estado == "Rejected":
            postulacion.assigned = False
            postulacion.accepted = estado
            postulacion.save()
            return Response({"message": "Postulacion de transporte rechazada"})
        else:
           return Response({"message": "Acccion de Postulacion de transporte no realizada"})

class EstadoEnvioLicitacionView(APIView):
    ''' Obtener un Envio segun id de la licitacion '''
    permission_classes = (permissions.AllowAny, )
    def get(self,request,licitacion):
        envioLicitacion = Envio.objects.filter(licitacion=licitacion).first()
        serializers = envioSerializer(envioLicitacion)
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



    



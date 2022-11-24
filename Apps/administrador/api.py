from .models import *
from rest_framework import viewsets, permissions 
from .serializers import *

class ContratoViewSet(viewsets.ModelViewSet):
    queryset= Contrato.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = ContratoSerializer



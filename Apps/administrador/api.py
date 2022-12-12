from .models import *
from rest_framework import viewsets, permissions 
from .serializers import *

class ContractViewSet(viewsets.ModelViewSet):
    queryset= Contract.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = ContractSerializer



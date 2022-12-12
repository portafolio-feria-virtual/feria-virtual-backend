from django.shortcuts import render
from .serializers import *
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import permissions
from Apps.productor.models import *
from rest_framework.response import Response
from Apps.productor.serializers import *

# Create your views here.
class CreateBuyingOfferView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BuyingOfferSerializer


class ListAllSalesAvailablesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            sales = LocalSale.objects.all().filter(sold = False)
            return LocalSaleSerializer(sales, many=True)

        except:
            return Response(status.HTTP_400_BAD_REQUEST)

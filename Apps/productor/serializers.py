from dataclasses import fields
from rest_framework import serializers
from .models import *
from Apps.comercianteLocal.serializers import *
from Apps.comercianteLocal.models import *


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    def validate_unitPrice (self, value):
        if value >0:
            return value
        else: 
            raise serializers.ValidationError('Unit price must be greater than 0')


class LocalSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalSale
        fields= ('__all__')
class AddLocalSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalSale
        fields= ("name","price", "stock","location","producer")

# class RetrieveLocalSaleImageSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField()

#     class Meta:
#         model = LocalSaleImage
#         fields = ("localSale","image","image_url")

#     def get_image_url_url(self, image):
#         request = self.context.get("request")
#         image_url = image.image.url
#         return request.build_absolute_uri(image_url)
class LocalSaleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalSaleImage
        fields = ("localSale","image")


class RestockLocalSale(serializers.ModelSerializer):

    class Meta:
        model = LocalSale
        fields = ("id","stock")

class SeeAllSalesWithBuyingOfferSerializer(serializers.ModelSerializer):
    #Para que aparezcan los datos realizado en serializador los modelos Offerss y PostulacionBidTransporte en el columna Bid debe agregar related_name=""
    #Los modelos Ofertas related_name="offers" y  PostulacionBidTransporte related_name="postulations"
    buyingoffers = BuyingOfferSerializer(many=True,read_only=True)
    class Meta:
        model= LocalSale
        fields= ("id","status", "sold","producer", "name", "price", "stock","location","closed", "confirmed", "buyingoffers")

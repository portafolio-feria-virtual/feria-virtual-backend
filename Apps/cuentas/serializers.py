
from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import *


# It creates a serializer for the UserAccount model.
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAccount
        fields = ('type','email', 'password',"firstName","lastName","address","phone","esComercianteExtranjero","esComercianteLocal","esConsultor","esProductor","esTransportista")
    password = serializers.CharField(
        min_length=8, write_only=True)

    def validate_password(self, value):
        return make_password(value)

class ChangePasswordSerializer(serializers.Serializer):
    model = UserAccount

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


# A serializer class that is used to convert the data into JSON format.
class ComercianteExtranjeroSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComercianteExtranjero
        fields=('email', 'password',"firstName","lastName","address","phone","country")

    password = serializers.CharField(
        min_length=8, write_only=True)

    def validate_password(self, value):
        return make_password(value)

# A serializer class that is used to serialize the data that is passed to the API.
class ComercianteLocalSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComercianteLocal
        fields=('email', 'password',"firstName","lastName","address","phone","documentNumber","businessName","rut")
    password = serializers.CharField(
        min_length=8, write_only=True)

    def validate_password(self, value):
        return make_password(value)
# A serializer class that will be used to create a new productor.
class ProductorSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productor
        fields=('email', 'password',"firstName","lastName","address","phone","documentNumber","businessName","rut","productType")
    password = serializers.CharField(
        min_length=8, write_only=True)

    def validate_password(self, value):
        return make_password(value)

# A serializer class that will be used to create a new transportista.
class TransportistaSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportista
        fields=('email', 'password',"firstName","lastName","address","phone","documentNumber","rut","capacity","size","cooling")
    password = serializers.CharField(
        min_length=8, write_only=True)

    def validate_password(self, value):
        return make_password(value)



    #es_comercianteExtranjero = models.BooleanField(default=True)
# class ClienteExternoSignupSerializer(serializers.ModelSerializer):
#     password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
#     class Meta:
#         model=UserAccount
#         fields=
#         extra_kwargs={
#             'password':{'write_only':True}
#         }
    
#     def save(self, **kwargs):
#         user=User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email']
#         )
#         password=self.validated_data['password']
#         password2=self.validated_data['password2']
#         if password !=password2:
#             raise serializers.ValidationError({"error":"password do not match"})
#         user.set_password(password)
#         user.is_freecancer=True
#         user.save()
#         Freelancer.objects.create(user=user)
#         return user

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

class ChangeEmailSerializer(serializers.Serializer):
    model = UserAccount

    """
    Serializer for email change endpoint.
    """
    email = serializers.CharField(required=True)


# A serializer class that is used to convert the data into JSON format.
class ComercianteExtranjeroSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComercianteExtranjero
        fields=('email', 'password',"firstName","lastName","businessName","address","phone","country")


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
        fields=('email', 'password',"firstName","lastName","address","phone","documentNumber","businessName","rut")
    password = serializers.CharField(
        min_length=8, write_only=True)

    def validate_password(self, value):
        return make_password(value)
class AdministradorSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields=('email', 'password',"firstName","lastName")
    password = serializers.CharField(
        min_length=8, write_only=True)

    def validate_password(self, value):
        return make_password(value)
class ConsultorSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultor
        fields=('email', 'password',"firstName","lastName")
    password = serializers.CharField(
        min_length=8, write_only=True)

    def validate_password(self, value):
        return make_password(value)



class UpdateEmailExtranjeroSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = ComercianteExtranjero
        fields = ( 'email',)
        

    def validate_email(self, value):
        user = self.context['request'].user
        if ComercianteExtranjero.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"Authorize":"You dont have permission for this user"})
        instance.email = validated_data['email']

        instance.save()

        return instance
class UpdateEmailLocalSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = ComercianteLocal
        fields = ( 'email',)
        

    def validate_email(self, value):
        user = self.context['request'].user
        if ComercianteLocal.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"Authorize":"You dont have permission for this user"})
        instance.email = validated_data['email']

        instance.save()

        return instance
class UpdateEmailProductorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = Productor
        fields = ( 'email',)
        

    def validate_email(self, value):
        user = self.context['request'].user
        if Productor.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"Authorize":"You dont have permission for this user"})
        instance.email = validated_data['email']

        instance.save()

        return instance
class UpdateEmailTransportistaSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = Transportista
        fields = ( 'email',)
        

    def validate_email(self, value):
        user = self.context['request'].user
        if Transportista.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"Authorize":"You dont have permission for this user"})
        instance.email = validated_data['email']

        instance.save()

        return instance

from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8, write_only=True)
    tipo_usuario = serializers.CharField(max_length=50)
	#id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True) 
	#id_user = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
    # 
    # 
    first_name = serializers.CharField(max_length=100, allow_blank= True )
    last_name = serializers.CharField(max_length=100, allow_blank= True)
    rut = serializers.CharField(
        max_length=11, allow_blank=True, required=False)
    address = serializers.CharField( max_length=50, allow_blank= True)
    phone = serializers.CharField(max_length=20, allow_blank= True)
    #is_active = serializers.BooleanField('Esta activo',default=True)
    #is_staff = serializers.BooleanField('Es administrador',default=False)
    tipos = (('0','Externo'),('1','Interno'),('2','Productor'),('3','Transportista'),('4','Consultor'),('5', "Administrador"))
    tipo_usuario = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=20, allow_blank= True)
    doc_num = serializers.CharField(
        max_length=9, allow_blank=True, required=False)
    business_name = serializers.CharField(
        max_length=100, allow_blank=True, required=False)
    capacity = serializers.CharField(
        max_length=20, allow_blank=True, required=False)
    prod_type = serializers.CharField(max_length=150, allow_blank= True, required=False)
    size = serializers.CharField(
        max_length=20, allow_blank=True, required=False)
    cooling = serializers.BooleanField(required=False)
    
    def validate_size(self, value):
        if not value:
            return 0
        try:
            return float(value)
        except ValueError:
            raise serializers.ValidationError("Se debe ingresar un entero")

    def validate_capacity(self, value):
        if not value:
            return 0
        try:
            return float(value)
        except ValueError:
            raise serializers.ValidationError("Se debe ingresar un decimal")


    class Meta:
        model = get_user_model()
        fields = ('tipo_usuario','email', 'rut','username', 'first_name','last_name', 'password', 'address', 'phone', 'country','doc_num','business_name','capacity','prod_type','size','cooling')


    def validate_password(self, value):
        return make_password(value)

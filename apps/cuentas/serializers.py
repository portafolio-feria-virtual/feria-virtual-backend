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

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'tipo_usuario')


    def validate_password(self, value):
        return make_password(value)

from django.shortcuts import render
from .serializers import *
from rest_framework import status, generics
from django.contrib.auth.decorators import user_passes_test
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


    



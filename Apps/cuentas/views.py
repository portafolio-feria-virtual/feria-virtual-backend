from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import status, generics
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth  import authenticate, login, logout
from rest_framework.response import Response
from .serializers import UserSerializer
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# class SignupView(generics.CreateAPIView):
#     serializer_class = UserSerializer


#@method_decorator(csrf_protect, name='dispatch')
class ExtranjeroSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ComercianteExtranjeroSignupSerializer

#@method_decorator(csrf_protect, name='dispatch')
class LocalSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ComercianteLocalSignupSerializer

#@method_decorator(csrf_protect, name='dispatch')
class ProductorSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProductorSignupSerializer

#@method_decorator(csrf_protect, name='dispatch')
class TransportistaSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = TransportistaSignupSerializer



@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        password = data['password']

        try:
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return Response({ 'success': 'User authenticated' })
            else:
                return Response({ 'error': 'Error Authenticating' })
        except:
            return Response({ 'error': 'Something went wrong when logging in' })






# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class GetCSRFToken(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def get(self, request, format=None):
#         return Response({ 'success': 'CSRF cookie set' })
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})

class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            logout(request)
            return Response({ 'success': 'Logout Out' })
        except:
            return Response({ 'error': 'Something went wrong when logging out' })



class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response({ 'isAuthenticated': 'success' })
            else:
                return Response({ 'isAuthenticated': 'error' })
        except:
            return Response({ 'error': 'Something went wrong when checking authentication status' })


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, ]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class GetCSRFToken(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def get(self, request, format=None):
#         return JsonResponse({ 'success': 'CSRF cookie set' })

class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user

        try:
            User.objects.filter(id=user.id).delete()

            return Response({ 'success': 'User deleted successfully' })
        except:
            return Response({ 'error': 'Something went wrong when trying to delete user' })
from .views import *
from django.urls import path, include


urlpatterns = [
#     path('auth/signup/',
#          SignupView.as_view(), name='signup'),
    path('auth/signupExt/',
         ExtranjeroSignupView.as_view(), name='signupExt'),
    path('auth/signupLoc/',
         LocalSignupView.as_view(), name='signupLoc'),
    path('auth/signupPro/',
          ProductorSignupView.as_view(), name='signupLoc'),
    path('auth/signupTra/',
         TransportistaSignupView.as_view(), name='signupTra'),

]
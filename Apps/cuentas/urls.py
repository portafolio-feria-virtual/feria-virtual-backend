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
     path('auth/login/',
         LoginView.as_view(), name='auth_login'),
         path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),
         path('auth/user/', CurrentUserView.as_view(), name= "user" ),
         path('auth/isAuthenticated/', CheckAuthenticatedView.as_view(), name= "user" ),
         path('auth/csrf_cookie', GetCSRFToken.as_view()),
         path('auth/delete', DeleteAccountView.as_view()),


]
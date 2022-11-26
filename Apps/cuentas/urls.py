from .views import *
from django.urls import path, include


urlpatterns = [
    path('auth/signupExt/', ExtranjeroSignupView.as_view(), name='signupExt'),
    path('auth/signupLoc/', LocalSignupView.as_view(), name='signupLoc'),
    path('auth/signupPro/', ProductorSignupView.as_view(), name='signupLoc'),
    path('auth/signupTra/', TransportistaSignupView.as_view(), name='signupTra'),
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/logout/',LogoutView.as_view(), name='auth_logout'),
    path('auth/user/', CurrentUserView.as_view(), name= "user" ),
    path('auth/isAuthenticated/', CheckAuthenticatedView.as_view(), name= "user" ),
    #path('auth/GetCsrf', GetCSRFToken.as_view()),
    path('auth/csrf_cookie', csrf),
    path('auth/ping', ping),
    path('auth/delete', DeleteAccountView.as_view()),
    path('auth/changePassword/', ChangePasswordView.as_view(), name='change-password'),
    path('auth/passwordReset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


]
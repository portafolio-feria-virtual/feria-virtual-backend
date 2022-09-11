
from .views import LoginView, LogoutView, SignupView, CurrentUserView
from django.urls import path, include

urlpatterns= [

    # path('api/v1/', include('djoser.urls')),
    # path('api/v1/', include('djoser.urls.authtoken'))
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('auth/signup/',
         SignupView.as_view(), name='auth_logout'),

    path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),

    path('auth/user/', CurrentUserView.as_view(), name= "user" )
]
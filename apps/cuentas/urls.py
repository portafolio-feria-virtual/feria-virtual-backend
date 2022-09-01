

from django.urls import path, include

cuentas_urlpatterns= [

    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken'))
]
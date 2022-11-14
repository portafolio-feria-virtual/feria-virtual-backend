from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Apps.cuentas.urls')),
    path('api/comercianteExtranjero/',include('Apps.comercianteExtranjero.urls')),
    path('api/comercianteLocal/',include('Apps.comercianteLocal.urls')),
    path('api/productor/',include('Apps.productor.urls')),
    path('api/transportista/',include('Apps.transportista.urls')),
    path('api/consultor/',include('Apps.consultor.urls')),
]



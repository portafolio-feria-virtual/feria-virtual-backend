from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Apps.cuentas.urls')),
    path('api/internationalTrader/',include('Apps.comercianteExtranjero.urls')),
    path('api/localTrader/',include('Apps.comercianteLocal.urls')),
    path('api/producer/',include('Apps.productor.urls')),
    path('api/carrier/',include('Apps.transportista.urls')),
    path('api/consultant/',include('Apps.consultor.urls')),

    path('api/administrator/',include('Apps.administrador.urls')),

    

    # # ...
    # # API Schema:
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # # Optional UI:
    # path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #     # ...



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




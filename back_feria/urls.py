from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Apps.cuentas.urls')),
    path('api/comercianteExtranjero/',include('Apps.comercianteExtranjero.urls')),
    path('api/comercianteLocal/',include('Apps.comercianteLocal.urls')),
    path('api/productor/',include('Apps.productor.urls')),
    path('api/transportista/',include('Apps.transportista.urls')),
    path('api/consultor/',include('Apps.consultor.urls')),

    path('api/administrador/',include('Apps.administrador.urls')),

    

    # ...
    # API Schema:
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
        # ...



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




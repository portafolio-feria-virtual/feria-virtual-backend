from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Apps.cuentas.urls')),
    path('api/comercianteExtranjero/',include('Apps.comercianteExtranjero.urls')),
    path('api/comercianteLocal/',include('Apps.comercianteLocal.urls')),
    path('api/productor/',include('Apps.productor.urls')),
    path('api/transportista/',include('Apps.transportista.urls')),
    path('api/consultor/',include('Apps.consultor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



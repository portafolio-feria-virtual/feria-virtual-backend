from .views import *
from django.urls import path, include

urlpatterns=[
    path('createLicitacion/', AddLicitacionView.as_view()),
    path('searchLicitacion/', SearchLicitacionView.as_view()),
    path('listLicitacion/<int:extranjero>', ListLicitacionView.as_view()),
    path('listOfertaProductorLicitacion/<int:licitacion>', ListOfertaProductorView.as_view()),
    path('listPostulacionTransportistaLicitacion/<int:licitacion>', ListPostulacionTransportistaView.as_view()),
    path('editLicitacion/<int:pk>',UpdateLicitacion.as_view()),
    path('extendCloseDateLicitacion/',EditCloseDateView.as_view()),
    path('aceptarOfertaProductor/',AceptarRechazarOfertaProductorView.as_view()),
    path('aceptarPostulacionTransportista/',AceptarRechazarPostulacionTrasporteView.as_view()),
    path('estadoEnvioLicitacion/<int:licitacion>',EstadoEnvioLicitacionView.as_view()),
    
]
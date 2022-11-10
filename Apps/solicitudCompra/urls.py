from .views import *
from django.urls import path, include

urlpatterns=[
    path('createSolicit/',
            SolicitudView.as_view())
]
from .views import *
from django.urls import path, include

urlpatterns=[
    path('createLicitacion/',
            AddLicitacionView.as_view())
]
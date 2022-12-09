import pytest
from rest_framework.test import APIClient
from Apps.cuentas.models import *
from Apps.administrador.models import *
from Apps.productor.models import *
from Apps.comercianteLocal.models import *
from Apps.comercianteExtranjero.models import *
from Apps.transportista.models import *


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def userExtranjero():
    datos = dict(
        email="wemake@bananas.com",
        password="toomuchbananas", 
        businessName="International Bananas Company",
        firstName="John", 
        lastName="Peers",
        address= "Fifth Avenue, Massachusetts", 
        phone= "56911111111", 
        country="United States"
    )

    extranjero = ComercianteExtranjero.objects.create(**datos)

    return extranjero

@pytest.fixture
def userLocal():
    datos = dict(
        email="webuy@bananas.com",
        password="notenoughbananas", 
        businessName="Compañia de Bananas Local",
        firstName="Juan", 
        lastName="Perez",
        address= "San Diego 4345, Santiago", 
        phone= "56911111111", 
        rut="20.333.444-1",
        documentNumber = "546234435"
    )

    local = ComercianteLocal.objects.create(**datos)

    return local

@pytest.fixture
def userProductor():
    datos = dict(
        email="weproduce@bananas.com",
        password="producingbananas", 
        businessName="Producción de bananas",
        firstName="Juan", 
        lastName="Perez",
        address= "San Fuente 3424, Santiago", 
        phone= "56911111111", 
        documentNumber="543644342",
        rut="32.432.432-3",
        productType="Bananas"
    )

    productor = Productor.objects.create(**datos)

    return productor

@pytest.fixture
def userTransportista():
    datos = dict(
        email="wetransport@bananas.com",
        password="movingbananas", 
        businessName="Transporte de bananas",
        firstName="John", 
        lastName="Peers",
        address= "Fifth Avenue, Massachusetts", 
        phone= "56911111111", 
        country="United States"
    )

    extranjero = ComercianteExtranjero.objects.create(**datos)

    return extranjero

@pytest.fixture
def userAdmin():
    datos = dict(
        email="wemake@bananas.com",
        password="toomuchbananas", 
        businessName="International Bananas Company",
        firstName="John", 
        lastName="Peers",
        address= "Fifth Avenue, Massachusetts", 
        phone= "56911111111", 
        country="United States"
    )

    extranjero = ComercianteExtranjero.objects.create(**datos)

    return extranjero

@pytest.fixture
def userConsultor():
    datos = dict(
        email="wemake@bananas.com",
        password="toomuchbananas"
    )

    extranjero = ComercianteExtranjero.objects.create(**datos)

    return extranjero

@pytest.fixture
def contrato(userExtranjero):
    datos = dict(
        type = "COMERCIANTE EXTRANJERO",
        companyName = "International Bananas Company",
        endDate = "2022-12-25",
        isActive = True,
        fileName = "JJJJJ"
    )
    contrato = Contrato.objects.create(**datos)

    return contrato

@pytest.fixture 
def ventaLocal(userProductor):
    datos = dict(
        status = "PUBLISHED",
        sold = False,
        name = "Venta de papas",
        price = 2500,
        stock = 1000,
        location = "Talagante"
    )
    ventaLocal = VentaLocal.objects.create(**datos)

    return ventaLocal
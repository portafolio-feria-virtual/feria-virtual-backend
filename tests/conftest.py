import pytest
from rest_framework.test import APIClient
from Apps.cuentas.models import *
from Apps.administrador.models import *
from Apps.productor.models import *
from Apps.comercianteLocal.models import *
from Apps.comercianteExtranjero.models import *
from Apps.transportista.models import *
import tempfile




@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def userExtranjero():
    data = dict(
        email="wemake@bananas.com",
        password="toomuchbananas", 
        businessName="International Bananas Company",
        firstName="John", 
        lastName="Peers",
        address= "Fifth Avenue, Massachusetts", 
        phone= "56911111111", 
        country="United States"
    )

    extranjero = InternationalTrader.objects.create(**data)

    return extranjero

@pytest.fixture
def userLocal():
    data = dict(
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

    local = LocalTrader.objects.create(**data)

    return local

@pytest.fixture
def userProductor():
    data = dict(
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

    productor = Producer.objects.create(**data)

    return productor

@pytest.fixture
def userTransportista():
    data = dict(
        email="wetransport@bananas.com",
        password="movingbananas", 
        businessName="Transporte de bananas",
        firstName="John", 
        lastName="Peers",
        address= "Fifth Avenue, Massachusetts", 
        phone= "56911111111", 
    )

    carrier = Carrier.objects.create(**data)

    return carrier

@pytest.fixture
def userAdmin():
    data = dict(
        email="wemake@bananas.com",
        password="toomuchbananas", 
        businessName="International Bananas Company",
        firstName="John", 
        lastName="Peers",
        address= "Fifth Avenue, Massachusetts", 
        phone= "56911111111", 
        country="United States"
    )

    administrator = Administrator.objects.create(**data)

    return administrator

@pytest.fixture
def userConsultor():
    data = dict(
        email="wemake@bananas.com",
        password="toomuchbananas"

    )

    extranjero = Consultant.objects.create(**data)

    return extranjero

@pytest.fixture
def contract(userExtranjero):
    #file = "tests/files/LESP05_U2_GA.pdf"
    data = dict(
        type = "INTERNATIONAL TRADER",
        companyName = "International Bananas Company",
        endDate = "2022-12-25",
        isActive = True,
        file = tempfile.NamedTemporaryFile(suffix=".pdf").name
    )
    contract = Contract.objects.create(**data)

    return contract

@pytest.fixture #Venta local
def localSale(userProductor):
    datos = dict(
        status = "PUBLISHED",
        producer = userProductor,
        sold = False,
        name = "Venta de papas",
        price = 2500,
        stock = 1000,
        location = "Talagante"
    )
    localSale = LocalSale.objects.create(**datos)

    return localSale

@pytest.fixture #Licitacion 
def bid(userExtranjero):
    datos = dict(
        name = "Compra de Bananas",
        description = "Compra de Bananas por International Bananas Company",
        country = "United States",
        region = "California",
        city = "Los Angeles",
        street = "Calle falsa 123",
        postalCode = "	90002",
        productList = "Bananas, Bananas pro max, Green Bananas",
        initDate = "2022-12-12",
        closeDate = "2022-12-28",
        maxAmount = 1000,
        internationalTrader = userExtranjero
    )
    licitacion = Bid.objects.create(**datos)
    print(licitacion.processStatus)
    return licitacion


@pytest.fixture # Crear oferta sin asignar
def offer(bid, userProductor):
    data = dict(
        producer = userProductor, 
        bid = bid,
        name = "Oferta de bananas",
        offerDescription = "Bananas promax",
        offerValue = 5000,
        offerFile = tempfile.NamedTemporaryFile(suffix=".pdf").name,
        assigned = False,
        status = "STANDBY",
        closed = False,
        confirmed = False
    )
    offer = Offer.objects.create(**data)

    return offer
@pytest.fixture #Licitacion 
def bidWithOffers(userExtranjero, offer):
    test1= offer
    test2 = offer
    datos = dict(
        name = "Compra de Bananas",
        description = "Compra de Bananas por International Bananas Company",
        country = "United States",
        region = "California",
        city = "Los Angeles",
        street = "Calle falsa 123",
        postalCode = "	90002",
        productList = "Bananas, Bananas pro max, Green Bananas",
        initDate = "2022-12-12",
        closeDate = "2022-12-28",
        maxAmount = 1000,
        internationalTrader = userExtranjero
    )
    licitacion = Bid.objects.create(**datos)

    return licitacion

@pytest.fixture #Oferta carrier
def carrierOffer(bid, userTransportista):
    data = dict(
        bid = bid,
        description = "Transporte de bananas",
        carrier = userTransportista,
        capacity = "5MIL BANANAS",
        cooling = True,
        price = 50000,
        assigned = False,
        accepted = "STANDBY"

    )
    carrierOffer = TransportPostulation.objects.create(**data)
    
    return carrierOffer

@pytest.fixture #Shipping
def shippingStatus(bid, userTransportista, userProductor):
    data = dict(
        status = "PREPARATION",
        bid= bid,
        editable = True,
        producer = userProductor,
        carrier=  userTransportista
    )
    shippingStatus = Shipping.objects.create(**data)

    return shippingStatus

@pytest.fixture #Oferta carrier aceptada
def carrierOfferAccepted(bid, userTransportista):
    data = dict(
        bid = 1,
        description = "Transporte de bananas",
        carrier = 1,
        capacity = "5MIL BANANAS",
        cooling = True,
        price = 50000,
        assigned = True,
        accepted = "ACCEPTED"

    )
    carrierOffer = TransportPostulation.objects.create(**data)
    
    return carrierOffer



import pytest 
from django.core.files.uploadedfile import SimpleUploadedFile
from Apps.productor.models import *

@pytest.mark.django_db #Ver licitaciones
def testViewBids (client, bid):
    response = client.get("/api/producer/seeAllBid")
    data = response.data
    print (data)
    assert data[0]["name"] == "Compra de Bananas"

@pytest.mark.django_db #Añadir oferta
def testAddOffer(client, userProductor, bid):
    file = "tests/files/LESP05_U2_GA.pdf"
    datos = dict(
        bid = bid.id,
        name = "Oferta por manzanas rojas",
        offerDescription = "Oferta por la mitad del stock de manzanas rojas",
        offerValue = 70000,
        offerFile =(open(file,'rb'),file)
    )
    response = client.post("/api/producer/createOffer", datos)
    data = response.data
    assert data["name"] == "Oferta por manzanas rojas"
    assert response.status_code == 201

@pytest.mark.django_db #Aceptar adjudicacion
def testAcceptBid (client,userProductor,bid, offer):
    datos = dict(
        id = bid,
        opt = "Accept"
    )
    response = client.post("/api/producer/acceptBid/", datos)
    data = response.data
    assert data["status"] == "ACCEPTED"

@pytest.mark.django_db #Ver estado transporte
def testCarrierStatus (client,userProductor, shippingStatus):
    response = client.get("/api/producer/packageTrackingGeneral/")
    data = response.data
    assert data[0]["status"] == "PREPARATION"



@pytest.mark.django_db #Añadir Venta local
def testAddSale (client, userProductor):
    datos = dict(
        producer = userProductor,
        name = "Venta de manazas",
        price = 1500,
        stock = 2500,
        location = "Calle falsa 123"
    )
    response = client.post("/api/producer/createSale", datos)
    data = response.data
    assert response.status_code == 201
    assert data["name"] == "Venta de manazas"
    assert data["stock"] == 2500

@pytest.mark.django_db #Ver ventas locales
def testViewLocalSales (client, userProductor, localSale):
    response = client.get("/api/producer/seeAllSales")
    data = response.data 
    assert response.status_code == 200
    assert data[0]["name"] == "Venta de papas"

@pytest.mark.django_db #Editar Venta Local
def testUpdateLocalSales (client, userProductor, localSale):
    datos = dict(
        id = localSale.id,
        producer = localSale.producer,
        status = "HAS_OFFER",
        sold = False,
        name = "Venta de tomates",
        price = 500,
        stock= 2500,
        location = "Chile",
        published = localSale.published,
        closed = False,
        editable = True,
        confirmed = False
    )
    response = client.put("/api/producer/updateSale", datos)
    data = response.data
    assert data["message"] == "Offer modified"




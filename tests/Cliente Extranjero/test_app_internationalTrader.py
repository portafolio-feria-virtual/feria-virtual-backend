import pytest 
from Apps.comercianteExtranjero.models import *

@pytest.mark.django_db #listar licitacion
def testListBids(client, userExtranjero, bid):
    datos = dict(
        internationalTrader = int(bid.internationalTrader.id)
    )
    print(datos["internationalTrader"])
    response = client.post("/api/internationalTrader/listBid/", datos)
    data = response.data
    print(data )
    assert data[0]["name"] == "Compra de Bananas"
    assert data[0]["description"] == "Compra de Bananas por International Bananas Company"

@pytest.mark.django_db #buscar licitacion
def testSearchBid(client, userExtranjero, bid):
    datos = dict(
        id = bid.id
    )
    response = client.post("/api/internationalTrader/searchBid/", datos)
    data = response.data
    assert data["name"] == "Compra de Bananas"     
    assert data["description"] == "Compra de Bananas por International Bananas Company"

@pytest.mark.django_db #crear licitacion
def testCreateBid(client, userExtranjero):
    bid = dict(
        name = "Proceso Venta Manzana",
        description = "Pedido 500kg manzana",
        country = "Argentina",
        region = "AR",
        city = "Buenos Aires",
        street = "Avenida Olivos 4109",
        postalCode = "B8000XAV",
        productList = "Manzanas Rojas",
        maxAmount = 1500,
        initDate = "2022-12-12",
        closeDate = "2023-01-10",
        #processStatus = "PUBLISHED",
        #editable = True,
        internationalTrader = userExtranjero.id
    )
    response = client.post("/api/internationalTrader/createBid/", bid)
    data = response.data
    assert data["name"] == "Proceso Venta Manzana"
    assert response.status_code == 201

@pytest.mark.django_db #postulante carrier
def testViewPostulant(client, userExtranjero, bid, carrierOffer):
    datos = dict(
        bid = bid.id 
    )
    response = client.post("/api/internationalTrader/listCarriersPostulation/", datos)
    data = response.data
    assert data [0]["description"] == "Transporte de bananas"
    assert data [0]["capacity"]  == "5MIL BANANAS"

@pytest.mark.django_db #lista ofertas
def testListOffersProducer(client, userExtranjero, offer, bid):
    datos = dict(
        bid = bid.id
    )
    response = client.post("/api/internationalTrader/listOffersProducer/", datos)
    data = response.data
    print(data)
    assert data[0]["name"] == "Oferta de bananas"
    assert data[0]["offerValue"] == 5000

@pytest.mark.django_db #editar fecha de cierre licitacion DIA/MES/AÑO
def testEditCloseDate(client, userExtranjero, bid):
    datos = dict(
        id = bid.id,
        closeDate = "29/12/2022"
    )
    response = client.post("/api/internationalTrader/extendCloseDateBid/", datos)
    data = response.data
    assert data["message"] == "Bid Date modified."
# @pytest.mark.django_db #editar fecha de cierre licitacion AÑO-MES-DIA
# def testEditCloseDate(client, userExtranjero, bid):
#     datos = dict(
#         id = 1,
#         closeDate = "2022-12-29"
#     )
#     response = client.post("/api/internationalTrader/extendCloseDateBid/", datos)
#     data = response.data
#     assert data["closeDate"] != "2022-12-28"

 
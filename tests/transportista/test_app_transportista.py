import pytest
from Apps.transportista.models import *

@pytest.mark.django_db #Listar licitaciones
def testViewBids(client, userTransportista, bid):
    response = client.get("/api/carrier/seeAllBidsAvailable/")
    data = response.data
    
    assert response.status_code == 200
    assert data[0]["name"] == "Compra de Bananas"

@pytest.mark.django_db #Aceptar licitacion
def testAcceptBid(client, userTransportista, carrierOffer):
    datos = dict(
        id= carrierOffer.id,
        opt = "Accept"
    )
    response = client.post("/api/carrier/acceptBid/", datos)
    data = response.data
    print (data)
    assert data["accepted"] == "ACCEPTED"

# @pytest.mark.django_db #Listar licitaciones aceptadas
# def testListAcceptedBids(client, userTransportista, shippingStatus): 
#     response = client.get("/api/carrier/seeAllPostulations/")
#     data = response.data
#     assert data["description"] == "Transporte de bananas"

@pytest.mark.django_db #Cambiar estado de envio
def testChangeTracking(client, userTransportista, shippingStatus):
    datos = dict(
        id = shippingStatus.id, 
    )
    response = client.post("/api/carrier/changeTracking/", datos)
    data = response.data
    assert data["status"] == "AWAITING_CARRIER"



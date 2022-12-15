import pytest
from Apps.comercianteLocal.models import *

@pytest.mark.django_db #Ver marketplace
def testSeeAllSales(client, userLocal, localSale):
    response = client.get("/api/localTrader/seeAllSalesAvailable/")
    data = response.data 
    #print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAA" + data)
    assert data[0]["name"] == "Venta de papas"

@pytest.mark.django_db #Crear offer
def testCreateBuyOffer(client, userLocal, localSale):
    datos = dict(
        localSale = localSale.id,
        localTrader = userLocal.id,
        status = "PUBLISHED",
        orderDate = "2022-12-24",
        editable = True,
        quantity = 100,
        confirmed = False
    )
    response = client.post("/api/localTrader/createBuyingOffer/", datos)
    data = response.data
    #print(data)
    assert data["quantity"] == 100
    assert response.status_code == 201

#@pytest.mark.django_db #

import pytest 
from Apps.administrador.models import Contract
import tempfile
import os



@pytest.mark.django_db #Crear contrato
def testCreateContract(client, userExtranjero):
    file = "tests/files/LESP05_U2_GA.pdf"
    contrato = dict(
        type = "INTERNATIONAL TRADER",
        companyName = userExtranjero.businessName,
        endDate = "2022-12-25",
        isActive = True,
        file = (open(file,'rb'),file)
    )
    response = client.post("/api/administrator/addContract/", contrato)
    data = response.data

    assert data["companyName"] == contrato["companyName"] 
    assert response.status_code == 201


@pytest.mark.django_db #Ver contratos
def testViewContract(client, contract):
    response = client.get("/api/administrator/viewAllContract/")
    data = response.data
    assert response.status_code == 200
    assert data[0]["companyName"] == "International Bananas Company"

@pytest.mark.django_db #Buscar contract
def testSearchContract(client, contract):
    datos = dict(
        companyName = "International Bananas Company"
    )
    response = client.post("/api/administrator/searchContract/", datos)
    data = response.data
    assert response.status_code == 200
    assert data["companyName"] == "International Bananas Company"
    assert data["endDate"] == contract.endDate

@pytest.mark.django_db #editar contrato
def testEditContract(client, contract):
    
    datos = dict(
        id = contract.id,
        endDate = "2022-12-26"
        
    )
    response = client.post("/api/administrator/editDateContract/", datos)
    data = response.data
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" + str(data))
    assert response.status_code == 200
    assert data["endDate"] != "2022-12-25"
    assert data["companyName"] == contract.companyName

@pytest.mark.django_db #Ver licitaciones 
def testViewBids(client, bid):
    response = client.get("/api/administrator/seeAllBids/")
    data = response.data
    print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" + str(data))
    assert response.status_code == 200
    assert data[0]["description"] == "Compra de Bananas por International Bananas Company"

@pytest.mark.django_db #Ver venta local 
def testViewLocalSale (client, localSale):
    response = client.get("/api/administrator/seeAllLocalSales/")
    data = response.data
    print ("AAAAAAAA2222222" + str(data))
    assert response.status_code == 200
    assert data[0]["name"] == "Venta de papas"
    
    

import pytest 
from Apps.administrador.models import Contrato

@pytest.mark.django_db 
def testCreateContract(client, userExtranjero):
    contrato = dict(
        type = "COMERCIANTE EXTRANJERO",
        companyName = "International Bananas Company",
        endDate = "2022-12-25",
        isActive = True,
        fileName = "JJJJJ"
    )
    response = client.post("/api/administrador/addContract/", contrato)
    data = response.data
    assert data["companyName"] == contrato["companyName"] 
    assert response.status_code == 201


@pytest.mark.django_db
def testViewContract(client, contrato):
    response = client.get("/api/administrador/viewContract/")
    data = response.data
    assert response.status_code == 200
    assert data[0]["companyName"] == "International Bananas Company"

@pytest.mark.django_db
def testSearchContract(client, contrato):
    datos = dict(
        companyName = "International Bananas Company"
    )
    response = client.post("/api/administrador/buscarContrato/", datos)
    data = response.data
    assert response.status_code == 200
    assert data["companyName"] == "International Bananas Company"
    assert data["endDate"] == contrato.endDate
    assert data["fileName"] == contrato.fileName

@pytest.mark.django_db
def testEditContract(client, contrato):
    datos = dict(
        id = 1,
        type = "COMERCIANTE EXTRANJERO",
        companyName = "International Bananas Company",
        endDate = "2022-12-26",
        isActive = True,
        fileName = "JJJJJ"
    )
    response = client.patch("/api/administrador/editarContrato/", datos)
    data = response.data
    assert response.status_code == 200
    assert data["endDate"] != "2022-12-25"
    assert data["companyName"] == contrato.companyName
    
    

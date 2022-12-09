import pytest
from rest_framework.test import APIClient



@pytest.mark.django_db
def testSignupExtranjero(client):
    payload = dict(
        email="email@email.com",
        password="password1", 
        businessName="International Bananas Company",
        firstName="Juan", 
        lastName="Perez",
        address= "Calle falsa 123", 
        phone= "56911111111", 
        country="Chile"
    )

    response = client.post("/api/auth/signupExt/", payload)

    data = response.data
    #assert response.status_code == 201, response.message
    assert data["firstName"]== payload["firstName"]

@pytest.mark.django_db
def test_login_extranjero(client,user_extranjero):
    

    response = client.post("/api/auth/login/",dict(email="wemake@bananas.com", password="toomuchbananas"))

    assert response.status_code==200
import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()

    yield client

def test_identify(client):
    payload = {
                "cpf": "93762814031",
                "celular": "71935228778"
    }

    request = client.post("/api/auth/identify",json=payload)
    assert  request.get_json().get("status") == 200
    assert  request.get_json().get("message") == "Client successfully identified"

def test_simulation(client):
    payload = {
                "cpf": "93762814031",
                "celular": "71935228778"
    }

    request = client.post("/api/auth/identify",json=payload)

    payload = {
                "numeroParcelas": 12,
                "valor": 10000
    }

    request = client.post("/api/loan/simulation", headers={'Authorization': request.get_json().get("token")}, json=payload)
    
    assert  request.get_json().get("numeroParcelas") == 12
    assert  request.get_json().get("outrasTaxas") == 85
    assert  request.get_json().get("total") == 10535.0
    assert  request.get_json().get("valorJuros") == 450.0
    assert  request.get_json().get("valorParcela") == 877.92
    assert  request.get_json().get("valorSolicitado") == 10000
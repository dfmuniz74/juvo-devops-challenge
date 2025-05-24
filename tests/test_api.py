import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_score_valido(client):
    response = client.get("/score/33333333333")
    assert response.status_code == 200
    assert isinstance(response.json['score'], int)

def test_cpf_invalido(client):
    response = client.get("/score/00000000000")
    assert response.status_code == 404
    assert response.json['erro'] == "CPF não encontrado"
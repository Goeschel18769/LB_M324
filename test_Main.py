import pytest
from Main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_without_name(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hallo, Welt!' in response.data

def test_index_with_name(client):
    response = client.get('/?name=Joel')
    assert response.status_code == 200
    assert b'Hallo, Joel!' in response.data 

def test_invalid_url(client):
    response = client.get('/invalid-url')
    assert response.status_code == 404
    assert b'Not Found' in response.data 
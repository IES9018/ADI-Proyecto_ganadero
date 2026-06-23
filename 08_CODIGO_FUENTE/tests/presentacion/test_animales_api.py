from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_animales():

    response = client.get("/animales")

    assert response.status_code == 200
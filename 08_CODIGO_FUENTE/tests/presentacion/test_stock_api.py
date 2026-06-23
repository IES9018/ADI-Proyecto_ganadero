from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_stock():

    response = client.get("/stock")

    assert response.status_code == 200
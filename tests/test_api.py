from fastapi.testclient import TestClient
from app.main import app

import pytest

@pytest.fixture

def client():
    return TestClient(app)

def test_predict_batch(client):
    response = client.post(
        "/predict",
        json={
  "area": 10000,
  "bedrooms": 4,
  "bathrooms": 4,
  "stories": 4,
  "mainroad": "yes",
  "guestroom": "yes",
  "basement": "yes",
  "hotwaterheating": "yes",
  "airconditioning": "yes",
  "parking": 4,
  "prefarea": "yes",
  "furnishingstatus": "furnished"
}
    )
    assert response.status_code==200
    data = response.json()
    assert "result" in data
    assert data["result"]
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def auth_headers(client):
    response = client.post("/auth/login", json={"username": "demo", "password": "password"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

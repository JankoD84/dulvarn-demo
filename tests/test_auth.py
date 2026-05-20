def test_login_success(client):
    response = client.post("/auth/login", json={"username": "demo", "password": "password"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials(client):
    response = client.post("/auth/login", json={"username": "wrong", "password": "wrong"})
    assert response.status_code == 401


def test_login_missing_fields(client):
    response = client.post("/auth/login", json={"username": "demo"})
    assert response.status_code == 422

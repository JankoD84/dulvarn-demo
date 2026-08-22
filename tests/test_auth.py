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


def test_login_returns_refresh_token(client):
    response = client.post("/auth/login", json={"username": "demo", "password": "password"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


def test_refresh_success(client):
    login_response = client.post("/auth/login", json={"username": "demo", "password": "password"})
    refresh_token = login_response.json()["refresh_token"]

    response = client.post("/auth/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"

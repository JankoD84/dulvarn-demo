def test_list_releases(client):
    response = client.get("/releases/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3


def test_get_release_found(client):
    response = client.get("/releases/1")
    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0"


def test_get_release_not_found(client):
    response = client.get("/releases/999")
    assert response.status_code == 404


def test_validate_release_blocked(client):
    response = client.post("/releases/3/validate")
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is False
    assert len(data["errors"]) > 0


def test_validate_release_ok(client):
    response = client.post("/releases/1/validate")
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is True

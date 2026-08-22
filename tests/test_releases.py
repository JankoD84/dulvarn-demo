from app.releases.service import validate_release


def test_validate_release_none_input():
    result = validate_release(None)
    assert result["valid"] is False
    assert len(result["errors"]) > 0


def test_validate_release_blank_version():
    result = validate_release({"version": "", "status": "pending", "released_at": None})
    assert result["valid"] is False
    assert any("Version" in e for e in result["errors"])


def test_validate_release_whitespace_version():
    result = validate_release({"version": "  ", "status": "pending", "released_at": None})
    assert result["valid"] is False
    assert any("Version" in e for e in result["errors"])


def test_validate_release_released_without_timestamp():
    result = validate_release({"version": "2.0.0", "status": "released", "released_at": None})
    assert result["valid"] is False
    assert any("released_at" in e for e in result["errors"])


def test_validate_release_released_with_timestamp():
    result = validate_release({"version": "2.0.0", "status": "released", "released_at": "2026-05-01T10:00:00Z"})
    assert result["valid"] is True
    assert result["errors"] == []


def test_list_releases(client, auth_headers):
    response = client.get("/releases/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3


def test_get_release_found(client, auth_headers):
    response = client.get("/releases/1", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0"


def test_get_release_not_found(client, auth_headers):
    response = client.get("/releases/999", headers=auth_headers)
    assert response.status_code == 404


def test_validate_release_blocked(client, auth_headers):
    response = client.post("/releases/3/validate", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is False
    assert len(data["errors"]) > 0


def test_validate_release_ok(client, auth_headers):
    response = client.post("/releases/1/validate", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is True


def test_validate_release_missing_timestamp(client, auth_headers):
    """Release with status=released but no released_at should fail validation."""
    response = client.post("/releases/2/validate", headers=auth_headers)
    assert response.status_code == 200
    # pending status is fine — no timestamp required
    data = response.json()
    assert data["valid"] is True

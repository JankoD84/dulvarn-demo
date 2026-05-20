from typing import Optional

MOCK_RELEASES = [
    {"id": 1, "version": "1.0.0", "status": "released", "released_at": "2026-05-01T10:00:00Z"},
    {"id": 2, "version": "1.1.0", "status": "pending", "released_at": None},
    {"id": 3, "version": "1.2.0", "status": "blocked", "released_at": None},
]


def get_all_releases() -> list:
    return MOCK_RELEASES


def get_release_by_id(release_id: int) -> Optional[dict]:
    for r in MOCK_RELEASES:
        if r["id"] == release_id:
            return r
    return None


def validate_release(release: dict) -> dict:
    errors = []

    if release is None:
        return {"valid": False, "errors": ["Release data is missing."]}

    if release.get("status") == "blocked":
        errors.append("Release is blocked — resolve blockers before proceeding.")

    version = release.get("version")
    if not version or not version.strip():
        errors.append("Version field is required and cannot be blank.")

    released_at = release.get("released_at")
    if release.get("status") == "released" and released_at is None:
        errors.append("Released status requires a released_at timestamp.")

    return {"valid": len(errors) == 0, "errors": errors}

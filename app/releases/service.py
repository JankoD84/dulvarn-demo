from typing import Optional
from datetime import datetime

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

    if release.get("status") == "blocked":
        errors.append("Release is blocked — resolve blockers before proceeding.")

    if not release.get("version"):
        errors.append("Version field is required.")

    return {"valid": len(errors) == 0, "errors": errors}

from fastapi import APIRouter, HTTPException
from app.releases.service import get_all_releases, get_release_by_id, validate_release

router = APIRouter()


@router.get("/")
def list_releases():
    return get_all_releases()


@router.get("/{release_id}")
def get_release(release_id: int):
    release = get_release_by_id(release_id)
    if not release:
        raise HTTPException(status_code=404, detail="Release not found")
    return release


@router.post("/{release_id}/validate")
def validate(release_id: int):
    release = get_release_by_id(release_id)
    if not release:
        raise HTTPException(status_code=404, detail="Release not found")
    return validate_release(release)

from fastapi import APIRouter, HTTPException, Depends
from app.releases.service import get_all_releases, get_release_by_id, validate_release
from app.middleware.auth import auth_required

router = APIRouter()


@router.get("/")
def list_releases(current_user: dict = Depends(auth_required)):
    return get_all_releases()


@router.get("/{release_id}")
def get_release(release_id: int, current_user: dict = Depends(auth_required)):
    release = get_release_by_id(release_id)
    if not release:
        raise HTTPException(status_code=404, detail="Release not found")
    return release


@router.post("/{release_id}/validate")
def validate(release_id: int, current_user: dict = Depends(auth_required)):
    release = get_release_by_id(release_id)
    if not release:
        raise HTTPException(status_code=404, detail="Release not found")
    return validate_release(release)

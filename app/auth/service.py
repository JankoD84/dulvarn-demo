from datetime import datetime, timedelta
from typing import Optional
import jwt
from app.core.config import settings

ALGORITHM = "HS256"

# Refresh token store (in-memory — replace with Redis in production)
_refresh_tokens: dict = {}


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.access_token_expire_minutes))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)


def create_refresh_token(username: str) -> str:
    expires = timedelta(days=7)
    token = create_access_token({"sub": username, "type": "refresh"}, expires_delta=expires)
    _refresh_tokens[username] = token
    return token


def rotate_refresh_token(old_token: str) -> Optional[dict]:
    """Validates old refresh token and issues new access + refresh token pair."""
    payload = verify_token(old_token)
    if not payload or payload.get("type") != "refresh":
        return None
    username = payload.get("sub")
    if not username or _refresh_tokens.get(username) != old_token:
        return None
    # Rotate: invalidate old, issue new
    new_access = create_access_token({"sub": username})
    new_refresh = create_refresh_token(username)
    return {"access_token": new_access, "refresh_token": new_refresh}


def verify_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def authenticate_user(username: str, password: str) -> bool:
    # Placeholder — replace with real DB lookup
    return username == "demo" and password == "password"

from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.service import verify_token

security = HTTPBearer()


class AuthMiddleware:
    """
    Reusable auth middleware. Extracts and validates Bearer token from request.
    Replaces inline token validation in individual route handlers.
    """

    def __init__(self, auto_error: bool = True):
        self.auto_error = auto_error

    async def __call__(self, request: Request) -> dict:
        credentials: HTTPAuthorizationCredentials = await security(request)
        if not credentials:
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not authenticated",
                )
            return {}

        token = credentials.credentials
        payload = verify_token(token)

        if payload is None:
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return {}

        return payload


auth_required = AuthMiddleware(auto_error=True)
auth_optional = AuthMiddleware(auto_error=False)

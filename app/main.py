from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.releases.routes import router as releases_router

app = FastAPI(title="Acme API", version="1.0.0")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(releases_router, prefix="/releases", tags=["releases"])


@app.get("/health")
def health():
    return {"status": "ok"}

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Acme API"
    secret_key: str = "dev-secret-key"
    access_token_expire_minutes: int = 30
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"


settings = Settings()

import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "notes-api"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change_me")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://neondb_owner:npg_L5iyMZgrvD3H@ep-cool-king-ad3h4dry-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require",
    )
    TEST_DATABASE_URL: str | None = os.getenv("TEST_DATABASE_URL")

settings = Settings()

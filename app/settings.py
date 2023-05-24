import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    TEST_BASE_NAME: str

    class Config:
        env_file = ".env"


setting = Settings()

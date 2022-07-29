import os
from pydantic import BaseSettings


class Config(BaseSettings):
    DEBUG: bool
    SECRET_KEY: str
    SQLALCHEMY_DATABASE_URI: str
    RESET_TOKEN: str
    VERIFICATION_TOKEN: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str = "HS256"

    class Config:
        env_file = f"{os.getcwd()}/.env"


Config = Config()

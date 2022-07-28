from distutils.command.config import config
from starlette.config import Config


config = Config('.env')


class Config(object):
    DEBUG = config("DEBUG", cast=bool)
    SECRET_KEY = config('SECRET_KEY', cast=str)
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', cast=str)
    RESET_TOKEN = config("RESET_TOKEN", cast=str)
    VERIFICATION_TOKEN = config("VERIFICATION_TOKEN", cast=str)
    ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int)
    ALGORITHM = "HS256"

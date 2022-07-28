from sqlalchemy import create_engine, MetaData
from databases import Database

from core.config import Config


SQLALCHEMY_DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

database = Database(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

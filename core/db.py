import os

from dotenv import load_dotenv
# import databases

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base    # DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from core.config import Config

load_dotenv()


SQLALCHEMY_DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,  # , connect_args={"check_same_thread": False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# database = databases.Database(SQLALCHEMY_DATABASE_URL)
# Base: DeclarativeMeta = declarative_base()

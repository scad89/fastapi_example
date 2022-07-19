import os

from dotenv import load_dotenv
# import databases

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base    # DeclarativeMeta
from sqlalchemy.orm import sessionmaker

load_dotenv()


SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,  # , connect_args={"check_same_thread": False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# database = databases.Database(SQLALCHEMY_DATABASE_URL)
# Base: DeclarativeMeta = declarative_base()

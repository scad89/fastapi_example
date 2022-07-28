from email.policy import default
from psycopg2 import Date
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = (DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

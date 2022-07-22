from core.db import Base
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String(30), nullable=False, unique=True)
    psw = Column(String(300), nullable=False)

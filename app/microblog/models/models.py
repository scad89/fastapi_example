from enum import unique
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from core.db import Base


class Post(Base):
    __tablename__ = 'microblog_posts'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    user = Column(Integer, ForeignKey('users.id'))
    user_id = relationship("User")

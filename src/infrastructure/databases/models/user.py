from ..db import Base
from sqlalchemy import Column, Integer, String, DateTime
import datetime


class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(255))
  email = Column(String(255))
  password = Column(String(255))
  created_at = Column(DateTime, default=datetime.datetime.now)
  updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
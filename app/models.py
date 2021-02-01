from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.types import Date
import datetime


Base = declarative_base()


class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    date_registered = Column(Date, default=datetime.date.today)

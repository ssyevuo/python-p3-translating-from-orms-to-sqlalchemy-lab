#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer, create_engine)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

engine = create_engine('sqlite:///dogs.db')
Session = sessionmaker(bind=engine)

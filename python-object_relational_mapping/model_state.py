#!/usr/bin/python3
"""module"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    """state class"""
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    email = Column(String(25), unique=True, nullable=False)
    favorites = relationship('Favorites', back_populates='user', uselist=True)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable = False)
    population = Column(Integer, nullable=False)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable = False)
    gender = Column(String(25), nullable = False)
    birth_year = Column(String(25), nullable = False)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)


#     def to_dict(self):
#         return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

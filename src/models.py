import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    firstname = Column(String(25), nullable=False)
    lastname = Column(String(25), nullable=False)
    email = Column(String(25), nullable=False)
# REVISAR EL UNIQUE EN email

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(Text, nullable=False)
    author_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    # type = Column(enumerate(iterable), nullable=False) **REVISAR EL ENUM
    url = Column(String(50), nullable=False)
    post_id = Column(Integer, nullable=False)


#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Enum
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
    email = Column(String(25), unique = True, nullable=False)
    follower= relationship('Follower',back_populates='user', uselist=True)
    

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('null'), nullable=False)
    url = Column(String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))


#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

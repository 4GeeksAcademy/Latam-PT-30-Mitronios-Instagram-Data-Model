import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(300), nullable=False)
    email = Column(String(400))
    password = Column(String(400))

# Relationship with Post
    posts = relationship("Post", back_populates="user")

# Relationship with Like
    likes = relationship("Like", back_populates="user")


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    description = Column(String(500))
    location = Column(String(150))

# Relationship with User
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="posts")

# Relationship with Comment
    comments = relationship("Comment", back_populates="post")

# Relationship with Like
    likes = relationship("Like", back_populates="post")


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    text = Column(String(500), nullable=False)
    post_id = Column(Integer)
    user_id = Column(Integer)

# Relationship with Post
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", back_populates="comments")


class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    user_id = Column(Integer)

# Relationship with post
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", back_populates=("likes"))

# Relationship with User
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates=("likes"))




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

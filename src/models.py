import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#class Person(Base):
#    __tablename__ = 'person'
#    # Here we define columns for the table person
#    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    name = Column(String(250), nullable=False)
#
#class Address(Base):
#    __tablename__ = 'address'
#    # Here we define columns for the table address.
#    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)
#
#    def to_dict(self):
#        return {}

class User(Base):
    __tablename__="user"

    id = Column(Integer, primary_key=True)
    userName = Column(String(120), unique=True, nullable = False)
    Password = Column(String(120), unique=False, nullable= False)

class Planet(Base):
    __tablename__="planet"

    id = Column(Integer, primary_key=True)
    Name = Column(String(120), unique=True, nullable = False)
    rotation_period = Column(Integer, unique=False, nullable=False)
    orbital_period = Column(Integer, unique=False, nullable=False)
    diameter = Column(Integer, unique=False, nullable=False)
    climate = Column(String(120), unique=False, nullable = False)
    gravity = Column(String(120), unique=False, nullable = False)
    surface_water = Column(Integer, unique=False, nullable=False)
    population = Column(Integer, unique=False, nullable=False)
    Favorites_id=Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship("Favorites",back_populates="planet")

class Character(Base):
    __tablename__="character"

    id = Column(Integer, primary_key = True)
    name = Column(String(120), unique=False, nullable = False)
    height = Column(Integer, unique=False, nullable=False)
    mass = Column(Integer, unique=False, nullable=False)
    hair_color = Column(String(120), unique=False, nullable = False)
    skin_color = Column(String(120), unique=False, nullable = False)
    eye_color = Column(String(120), unique=False, nullable = False)
    birth_year = Column(String(120), unique=False, nullable = False)
    homeWorld = Column(String(120), unique=False, nullable = False)
    Favorites_id=Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship("Favorites",back_populates="character")

class Favorites(Base):
    __tablename__="favorites"

    id = Column(Integer, primary_key = True)
    Planets = Column(String(120), unique=True, nullable = True)
    Character = Column(String(120), unique=True, nullable = True)
    User_id=Column(Integer, ForeignKey("user.id"))
    favorites = relationship("User",back_populates="favorites")   #nota en relationship el primer nombre es clase por eso va en mayus, el segundo nombre de back populates es nombre de tabla por eso en minuscula

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

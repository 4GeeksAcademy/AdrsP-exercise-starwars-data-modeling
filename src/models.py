import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__="user"

    id = Column(Integer, primary_key=True)
    userName = Column(String(120), unique=True, nullable = False)
    Password = Column(String(120), unique=False, nullable= False)

class Planet(Base):
    __tablename__="planet"

    id = Column(Integer, primary_key=True)
    planetName = Column(String(120), unique=True, nullable = False)
    solarSystem = Column(String(120), unique=False, nullable = False)
    galaxy = Column(String(120), unique=False, nullable = False)
    Atmosphere = Column(String(120), unique=False, nullable = False)

class Character(Base):
    __tablename__="character"

    CharacterId = Column(Integer, primary_key = True)
    Name = Column(String(120), unique=False, nullable = False)
    BornPlanet = Column(String(120), unique=False, nullable = False)
    Race = Column(String(120), unique=False, nullable = False)
    Profession = Column(String(120), unique=False, nullable = False)
    Affiliation = Column(String(120), unique=False, nullable = False)

class Favorites(Base):
    __tablename__="favorites"

    FavoritesId = Column(Integer, primary_key = True)
    Planets = Column(String(120), unique=True, nullable = False)
    Character = Column(String(120), unique=True, nullable = False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

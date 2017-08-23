import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


########## classes ##########

class Restaurant(Base):
  __tablename__ = 'restaurant'

  id = Column(Integer, primary_key=True)
  name = Column(String(80), nullable=False)
  user_id = Column(Integer, ForeignKey('user.id'))

  @property
  def serialize(self):
    return {
      'id' : self.id,
      'name' : self.name
    }

class MenuItem(Base):
  __tablename__ = 'menu_item'

  id = Column(Integer, primary_key=True)
  name = Column(String(80), nullable=False)
  course = Column(String(250))
  description = Column(String(250))
  price = Column(String(8))
  restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
  restaurant = relationship(Restaurant)
  user_id = Column(Integer, ForeignKey('user.id'))

  @property
  def serialize(self):
    return {
      'id' : self.id,
      'name' : self.name,
      'description' : self.description,
      'price' : self.price,
      'course' : self.course
    }

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  name = Column(String(80), nullable=False)
  email = Column(String(250), nullable=False)
  picture = Column(String(250), nullable=False)

######### /classes ##########


engine = create_engine('sqlite:///restaurantmenuwithusers.db')

Base.metadata.create_all(engine)

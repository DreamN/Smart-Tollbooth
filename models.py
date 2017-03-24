#################################################################
##      Create Database for the Smart Tollbooth Project        ##
#################################################################
import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from settings import getDatabaseString

Base = declarative_base()
engine = create_engine(getDatabaseString())
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Car(Base):
    # id on the license plate
    # owner is the name of car owner
    # rfid_id is the id of rfid card

    __tablename__ = 'car'
    id = Column(String(10), primary_key=True)
    owner = Column(String(250), nullable=False)
    rfid_id = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'owner': self.owner,
            'rfid_id': self.rfid_id,
        }


class CarInParking(Base):

    __tablename__ = 'car_in_parking'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    car_id = Column(Integer, ForeignKey('car.id'))
    car = relationship(Car)

Base.metadata.create_all(engine)

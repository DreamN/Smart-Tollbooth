#################################################################
##      Create Database for the Smart Tollbooth Project        ##
#################################################################
import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
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
    is_parking = Column(Boolean, default=False)

    def changeIsParking(self):
        self.is_parking = not self.is_parking
        print self.is_parking

    @property
    def serialize(self):
        return {
            'id': self.id,
            'owner': self.owner,
            'rfid_id': self.rfid_id,
        }


class Transaction(Base):

    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    car_id = Column(String(10), ForeignKey('car.id'))
    car = relationship(Car)
    status = Column(String(10))
    picture = Column(String(150))

    def __init__(self, car, picture):
        self.picture = picture
        self.car = car
        if car.is_parking:
            self.status = 'Come In'
        else:
            self.status = 'Go Out'

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'timestamp' : self.timestamp,
            'car_id' : self.car_id,
            'status' : self.status,
            'picture' : self.picture,
        }



Base.metadata.create_all(engine)

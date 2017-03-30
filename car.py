#################################################################
##                  SMART TOLLBOOTH PROJECT                    ##
#################################################################

from flask import Flask, jsonify
from sqlalchemy import create_engine
from models import Base, engine, session, Car, CarInParking
from prettytable import PrettyTable
import time


app = Flask(__name__)

class bcolors:
    REDFAIL = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


#+-----------------------------------------------------+#
#|                 Function Declaration                +#
#+-----+-----------------------------------------------+#
#|  #  |                    Function                   |#
#+-----+-----------------------------------------------+#
#|  1  |   insertCarParking(car)                       |#
#|  2  |   removeCarParking(car)                       |#
#|  3  |   printCarList()                              |#
#|  4  |   printCarParkingList()                       |#
#|  5  |   printInfo()                                 |#
#|  6  |   addCar(car_id, car_owner, car_rfid_id)      |#
#|  7  |   carComing(rfid_id)                          |#
#+-----+-----------------------------------------------+#

def insertCarParking(car):
    newCar = CarInParking(car = car)
    session.add(newCar)
    session.commit()
    print 'Inserted %s to the parking' % car.id

def removeCarParking(car):
    deleteCar = session.query(CarInParking).filter_by(car = car).one()
    session.delete(deleteCar)
    session.commit()
    print '%s is removed from the parking' % deleteCar.car_id

def printCarList():
    car_list = session.query(Car).all()
    table = PrettyTable(['ID', 'OWNER', 'RFID ID', 'IS PARKING'])
    table.align["ID"] = "l"
    table.padding_width = 1
    print 'There\'s a %d car in the system.' % len(car_list)
    for car in car_list:
        table.add_row([car.id, car.owner, car.rfid_id, car.is_parking])
    print table
    print '\n\n\n'

def printCarParkingList():
    parking_list = session.query(CarInParking).all()
    table = PrettyTable(['ID', 'TIMESTAMP', 'CAR_ID'])
    table.align["ID"] = "l"
    table.padding_width = 1
    print 'There\'s a %d car in parking.' % len(parking_list)
    for car in parking_list:
        table.add_row([car.id, car.timestamp, car.car_id])
    print table
    print '\n\n\n'

def printInfo():
    printCarList()
    printCarParkingList()

def addCar(car_id, car_owner, car_rfid_id):
    try:
        newCar = Car(id = car_id, owner = car_owner, rfid_id = car_rfid_id)
        session.add(newCar)
        session.commit()
        print 'Registered the car %s into the system' % car_id
    except:
        print 'Can\'t add this car....\n\t error happens'
    print '\n\n\n'

def carComing(rfid_id):
    print 'the rfid : %s is coming....' % rfid_id
    try:
        car = session.query(Car).filter_by(rfid_id = rfid_id).one()
    except:
        print 'Car Not Found'
        print '\n\n\n'
        return False
    if car.is_parking:
        print 'is this car id "%s"? and go out?' % car.id
    else:
        print 'is this car id "%s"? and come in?' % car.id
    match = ''
    while match != 'Y' and match != 'N':
        match = raw_input(bcolors.WARNING + "Please enter.... [Y]es / [N]o :" + \
                bcolors.ENDC).upper()
    if match == 'Y':
        car.is_parking = not car.is_parking
        session.add(car)
        session.commit()
        if car.is_parking:
            insertCarParking(car)
        else:
            removeCarParking(car)
        print bcolors.OKGREEN + 'Access Granted!!' + bcolors.ENDC
        servo.openBarrier()
        time.sleep(4)
        servo.closeBarrier()

    else:
        print bcolors.REDFAIL + 'Access Denied!!' + bcolors.ENDC
    print '\n\n\n'

#################################################################
##                  SMART TOLLBOOTH PROJECT                    ##
#################################################################

from flask import Flask, jsonify
from sqlalchemy import create_engine
from models import Base, engine, session, Car, CarInParking
from prettytable import PrettyTable


app = Flask(__name__)

class bcolors:
    REDFAIL = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


#+-----------------------------------------------------+#
#|                 Function Declaration                +#
#+-----------------------------------------------------+#
def printInfo():
    printCarList()
    printCarParkingList()

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
    table = PrettyTable(['ID', 'OWNER', 'RFID_ID'])
    table.align["ID"] = "l"
    table.padding_width = 1
    print '\n\n\nThere\'s a %d car in the system.' % len(car_list)
    for car in car_list:
        table.add_row([car.id, car.owner, car.rfid_id])
    print table

def printCarParkingList():
    parking_list = session.query(CarInParking).all()
    table = PrettyTable(['ID', 'TIMESTAMP', 'CAR_ID'])
    table.align["ID"] = "l"
    table.padding_width = 1
    print '\n\n\nThere\'s a %d car in parking.' % len(parking_list)
    for car in parking_list:
        table.add_row([car.id, car.timestamp, car.car_id])
    print table

def addCar(car_id, car_owner, car_rfid_id):
    try:
        newCar = Car(id = car_id, owner = car_owner, rfid_id = car_rfid_id)
        session.add(newCar)
        session.commit()
    except:
        print 'Can\'t add this car....\n\t error happens'

def printInfo():
    printCarList()
    printCarParkingList()

def carComing(rfid_id):
    print 'the rfid : %s is coming....' % rfid_id
    try:
        car = session.query(Car).filter_by(rfid_id = rfid_id).one()
    except:
        print 'Car Not Found'
        return False
    print 'is this car id "%s" ?' % car.id
    match = ''
    while match != 'Y' and match != 'N':
        match = raw_input(bcolors.WARNING + "Please enter.... [Y]es / [N]o :" + \
                bcolors.ENDC).upper()
    if match == 'Y':
        insertCarParking(car)
        print bcolors.OKGREEN + 'Access Granted!!' + bcolors.ENDC
    else:
        print bcolors.REDFAIL + 'Access Denied!!' + bcolors.ENDC


#+-----------------------------------------------------+#
#|                     Flask's View                    +#
#+-----------------------------------------------------+#
@app.route('/')
def index():
    return 'Welcome to Smart Tollbooth'

#+-----------------------------------------------------+#
#|                  Start-Up Statement                 +#
#+-----------------------------------------------------+#

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

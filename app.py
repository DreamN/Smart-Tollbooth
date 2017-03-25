#################################################################
##                  SMART TOLLBOOTH PROJECT                    ##
#################################################################

from flask import Flask, jsonify
from sqlalchemy import create_engine
from models import Base, engine, session, Car, CarInParking


app = Flask(__name__)

#+-----------------------------------------------------+#
#|                 Function Declaration                +#
#+-----------------------------------------------------+#
def printInfo():
    printCarList()
    printCarParkingList()

def insertCarParking(car_id):
    car = session.query(Car).filter_by(id = car_id).one()
    newCar = CarInParking(car = car)
    session.add(newCar)
    session.commit()
    print 'Inserted %s to the parking' % car.id

def removeCarParking(car_id):
    deleteCar = session.query(CarInParking).filter_by(car_id = car_id).one()
    session.delete(deleteCar)
    session.commit()
    print '%s is removed from the parking' % car.id

def printCarList():
    car_list = session.query(Car)
    print '\n\n\n<================================>'
    print 'There\'s a %d car in the system.' % len(car_list)
    for car in car_list:
        print '%s %s %s' % (car.id, car.owner, car.rfid_id)

def printCarParkingList():
    print '\n\n\n<================================>'
    parking_list = session.query(CarInParking)
    print 'There\'s a %d car in parking.' % len(car_in_parking)
    for car in parking_list:
        print '%s %s %s' % (car.id, car.owner, car.rfid_id)

def addCar(car_id, car_owner, car_rfid_id):
    try:
        newCar = Car(id = car_id, owner = car_owner, rfid_id = car_rfid_id)
        session.add(newCar)
        session.commit()
    except:
        print 'Can\'t add this car....\n\t error happens'

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

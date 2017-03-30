#################################################################
##                  SMART TOLLBOOTH PROJECT                    ##
#################################################################

from flask import Flask, jsonify
from sqlalchemy import create_engine
from models import Base, engine, session, Car, CarInParking
from prettytable import PrettyTable
from RFID import Rfid_Th
from car import *
import servo
import time


app = Flask(__name__)

class bcolors:
    REDFAIL = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


#+-----------------------------------------------------+#
#|                     Flask's View                    +#
#+-----------------------------------------------------+#
#| # |       PATH       |         Function             |#
#+---+------------------+------------------------------+#
#|  1| /                |  index()                     |#
#+---+------------------+------------------------------+#

@app.route('/')
def index():
    return 'Welcome to Smart Tollbooth'


#+-----------------------------------------------------+#
#|                  Start-Up Statement                 +#
#+-----------------------------------------------------+#
#Close the barrier when start
servo.closeBarrier()
Rfid_Th()
# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=80)

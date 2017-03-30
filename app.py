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
import thread

app = Flask(__name__)

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
thread.start_new_thread(Rfid_Th)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

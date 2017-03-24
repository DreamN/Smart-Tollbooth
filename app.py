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

#################################################################
##                  SMART TOLLBOOTH PROJECT                    ##
#################################################################

import sys
sys.path.insert(0, '../')

from flask import Flask, jsonify, send_from_directory, render_template
from sqlalchemy import create_engine
# from models import Base, engine, session, Car, CarInParking

app = Flask(__name__, static_folder='statics')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(app.static_folder + '/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(app.static_folder + '/css', path)

#+-----------------------------------------------------+#
#|                     Flask's View                    +#
#+-----------------------------------------------------+#
#| # |       PATH       |         Function             |#
#+---+------------------+------------------------------+#
#|  1| /                |  index()                     |#
#+---+------------------+------------------------------+#

@app.route('/')
def index():
    return render_template('index.html')


#+-----------------------------------------------------+#
#|                  Start-Up Statement                 +#
#+-----------------------------------------------------+#
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

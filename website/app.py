#################################################################
##                  SMART TOLLBOOTH PROJECT                    ##
#################################################################

import sys
sys.path.insert(0, '../')
from models import Base, engine, session, Car, Transaction
from flask import Flask, jsonify, send_from_directory, render_template
from sqlalchemy import create_engine
import psycopg2
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

@app.route('/transaction')
def transaction():
    transactions = session.query(Transaction).all()
    for t in transactions:
        print t.car_id
    return render_template('transactionlist.html', transactions = transactions)


#+-----------------------------------------------------+#
#|                  Start-Up Statement                 +#
#+-----------------------------------------------------+#
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

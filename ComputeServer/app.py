#################################################################
##                  SMART TOLLBOOTH CSERVER                    ##
#################################################################
from flask import Flask, jsonify, send_from_directory, render_template, request
from models import Base, engine, session, Car, Transaction
from werkzeug import secure_filename
from sqlalchemy import create_engine
import paho.mqtt.client as mqtt
import psycopg2
import datetime
import json
import time
import os
# from models import Base, engine, session, Car, CarInParking

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = '.'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

# MQTT configuration
client = mqtt.Client()
client.username_pw_set("tbcs", "random")
client.connect('m13.cloudmqtt.com', 11675, 60)
client.loop_start()

def allowed_file(filename):
	return '.' in filename and \
	filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def convert_timedelta(duration):
	days, seconds = duration.days, duration.seconds
	minutes = (days*1440) + seconds/60
	return minutes

def timedelta_to_fee(t):
	# 20 bath per hours
	fee = 20 * ((t/60) + 1)
	return fee

#+-----------------------------------------------------+#
#|                     Flask's View                    +#
#+-----------------------------------------------------+#
#| # |       PATH       |         Function             |#
#+---+------------------+------------------------------+#
#|  1| /                |  index()                     |#
#+---+------------------+------------------------------+#


@app.route('/')
def index():
    return 'Smart Tollbooth compute_server'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/carComing", methods=['POST'])
def carComing():
    if request.method == 'POST':
        car_rfid = request.form.get('car_rfid')
        print car_rfid
        file = request.files['file']
        if file and allowed_file(file.filename):
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print "https://smarttbcser.herokuapp.com/uploads/" + filename
        pic = "https://smarttbcser.herokuapp.com/uploads/" + filename

        try:
            car = session.query(Car).filter_by(rfid_id = car_rfid).one()
            status = ""
            if car.is_parking:
                status = "Go Out"
				car.changeIsParking()
				latest = session.query(Transaction).filter_by(car_id = car.id).order_by(Transaction.timestamp.desc()).first()
				print 'Latest time is: ' + str(latest.timestamp)
				print 'Current Time is: ' + str(datetime.datetime.utcnow())
				m = convert_timedelta(datetime.datetime.utcnow() - latest.timestamp)
				print 'Time delta is: ' + str(m)
				fee = timedelta_to_fee(m)
				print 'fee : ' + str(fee)
            else:
                status = "Come In"
				fee = 0
            print status
            newTrans = Transaction(car = car, picture = pic, status = status)
            #send mqtt to website
            data = {'id': car.id, 'pic': pic, 'driver': car.owner,
                   'timestamp': str(datetime.datetime.now()), 'fee': fee}
            s = json.dumps(data)
            print s
            client.publish("/CAR/IN", s)
            session.add(newTrans)
            session.commit()
        except:
            print 'car not found'
            #send mqtt to website
            data = {'id': 'Car not found', 'pic': "http://placehold.it/800x600",
                   'driver': '-', 'timestamp': '-'}
            s = json.dumps(data)
            print s
            client.publish("/CAR/IN", s)
    return 'Done'

def acceptCar(id):
    car = session.query(Car).filter_by(id = id).one()
    print 'got car'
    car.is_parking = not car.is_parking
    session.add(car)
    session.commit()
    print 'done commit'
    #Send MQTT to RPI





#+-----------------------------------------------------+#
#|                  Start-Up Statement                 +#
#+-----------------------------------------------------+#
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

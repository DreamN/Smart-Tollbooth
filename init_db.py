import psycopg2
from settings import getDatabaseString
from car import *
import os

def dropTable():
    try:
        conn = psycopg2.connect(getDatabaseString())
        cur = conn.cursor()
        sql_command = 'DROP TABLE car_in_parking;'
        sql_command += 'DROP TABLE car;'
        cur.execute(sql_command)
        conn.commit()
        print 'Drop table success!'
    except:
        print "Error happens (Drop table)"

def createTable():
    try:
        os.system('python models.py')
        print 'Create table success!'
    except:
        print "Error happens (Create table)"

def insertCar():
    addCar('SX9273', 'Peter Quill', '48,71,117,77')
    addCar('TA2837', 'Stephen Strange', '41,221,47,91')
    addCar('ML2837', 'Blackagar Boltagon', '21,35,129,203')
    addCar('SY8347', 'Daniel Rand', '233,77,128,203')

dropTable()
createTable()
printInfo()
insertCar()
carComing('SuxannsFcsjFxkxahiduenf')
carComing('E9cjnAusjwwksa84h8htjt8')
carComing('wmzidnvSzhdikwlskaLsisj')
carComing('E9cjnAusjwwksa84h8htjt8')
carComing('E9cjnAusjwwksa84h8htjt8')
printInfo()

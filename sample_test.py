import psycopg2
from settings import getDatabaseString
from app import *
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
    addCar('SX9273', 'Peter Quill', '18jsabD8ahdmw9xoamdjsTz')
    addCar('TA2837', 'Stephen Strange', 'wmzidnvSzhdikwlskaLsisj')
    addCar('AP2843', 'Tony Stark', 'SuxannsFcsjFxkxahiduenf')
    addCar('ML2837', 'Blackagar Boltagon', 'WlsmjfihnsA8xh3nf92dnks')
    addCar('MG2831', 'Thor Odinson', 'Azhw7dSxuujw9d8u4jg9dj5')
    addCar('AH3928', 'Peter Parker', 'Ss9tB9cjrmgo89n4igue8fj')
    addCar('SY8347', 'Daniel Rand', 'E9cjnAusjwwksa84h8htjt8')

dropTable()
createTable()
printInfo()
insertCar()
insertCarParking('AP2843')
insertCarParking('SY8347')
insertCarParking('SX9273')
removeCarParking('SY8347')
insertCarParking('AH3928')
printInfo()

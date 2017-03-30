#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import psycopg2
from settings import getDatabaseString
from app import *
import os
import MFRC522
import signal
import time


Buzzer = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Buzzer, GPIO.OUT)

continue_reading = True


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

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()
    printInfo()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

dropTable()
createTable()
insertCar()
printInfo()
# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

GPIO.output(Buzzer, GPIO.LOW)
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        suid = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        print "Card read UID: " + suid

        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print "Authentication error"
        GPIO.output(Buzzer, GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output(Buzzer, GPIO.LOW)
        carComing(suid)

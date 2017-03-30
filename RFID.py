#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import psycopg2
from settings import getDatabaseString
from car import *
import os
import MFRC522
import signal
import time


Buzzer = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Buzzer, GPIO.OUT)

continue_reading = True

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

def Rfid_Th():
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

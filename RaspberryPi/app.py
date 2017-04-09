#################################################################
##                  SMART TOLLBOOTH PROJECT                    ##
#################################################################

#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from picamera import PiCamera
from threading import Thread
import os
import requests
import MFRC522
import signal
import time
import servo


Buzzer = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Buzzer, GPIO.OUT)
continue_reading = True
CSERVER_URL = "https://smarttbcser.herokuapp.com/carComing"

# Ultrasonic
ECHO = 16
TRIG = 18
GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)
GPIO.setup(ECHO,GPIO.IN)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print 'Response : accept_' + str(msg.payload)
    acceptCar()

# MQTT configuration
client = mqtt.Client()
client.username_pw_set("tbrpi", "random")
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('m13.cloudmqtt.com', 11675, 60)
client.subscribe("/CAR/RES")
client.loop_start()

camera = PiCamera()
camera.resolution = (800, 600)

def read_distance():
    print 'Read Distance'
    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG,0)
    while GPIO.input(ECHO)== 0:
        pass
    start = time.time()
    while GPIO.input(ECHO)== 1:
        pass
    stop = time.time()
    return (stop - start) * 17000

def acceptCar():
    print 'Access Granted!!'
    servo.openBarrier()
    while(1):
        if(read_distance()<=8):
            print 'car\'s come'
            time.sleep(0.8)
            while(read_distance()<=8):
                print 'car\'s here'
                time.sleep(0.8)
            servo.closeBarrier()
            print 'done'
            break
        else:
            print 'wait for car'

def TakePic():
        takeTime = time.strftime("%d-%m-%Yh%Hm%Ms%S", time.localtime())
        path = "/home/pi/Pictures/"+takeTime+".jpg"
        print("TAKING PICTURE...")
        camera.capture(path)
        print("COMPLETE TAKE PICTURE!\n")
        return path

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

def rfid():
    while continue_reading:
        time.sleep(0.5)
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
            #TAKE PIC
            pathFile = TakePic()
            print pathFile
            #POST to CSERVER
            pic_file = {'file': open(pathFile, 'rb')}
            r = requests.post(CSERVER_URL, data={'car_rfid': suid}, files = pic_file)
            print 'done'


# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

servo.closeBarrier()
# Welcome message
print "Welcome to the Smart Tollbooth system"
print "Press Ctrl-C to stop."

GPIO.output(Buzzer, GPIO.LOW)
rfid()
